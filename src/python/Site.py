# Site.py
# management of HTTP(S) requests and the MVC interface

# Profess Copyright (c) 2019 Joshua 'joshuas3' Stockin
# <https://github.com/JoshuaS3/profess/>.


# This file is part of Profess.

# Profess is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Profess is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Profess. If not, see <https://www.gnu.org/licenses/>.

import os
from .types import *
from .SiteConfig import *
from .Model import *
from .View import *
from .Controller import *
from .Request import *
from .Response import *
from .MimeTypes import *
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

class Site:
	_config = None
	__running = False
	__server = None
	__site = None

	def __init__(self, config):
		types(SiteConfig, config)
		self._config = config
		self.__site = self

	def Start(self):
		types(SiteConfig, self._config)
		if self.__running:
			raise Exception("Server is already running")

		class RequestHandler(BaseHTTPRequestHandler):
			def _component_handler(self, view, request, response):
				if response.Sent:
					return

				compiledContent = ""
				isBinary = False
				if view.TemplateFile:
					for mimeType in MimeTypes:
						if mimeType["mime"] == view.MimeType:
							if mimeType["binary"]:
								isBinary = True
							break
					if not isBinary:
						_f = open(view.TemplateFile, "r")
						compiledContent = _f.read()
						_f.close()
					else:
						_f = open(view.TemplateFile, "rb")
						compiledContent = _f.read()
						_f.close()
						response.Mime = view.MimeType
						response.Content = compiledContent
						return
				else:
					compiledContent = view.TemplateString


				controllerVars = {}
				if view.ControllerID:
					_controller = self.siteObj.GetController(view.ControllerID)
					if _controller:
						_controllerVars = _controller.Handler(request, response)
						if (response.Sent):
							return
						controllerVars.update(_controllerVars)
				for varName in controllerVars:
					compiledContent = compiledContent.replace("@{" + varName + "}", str(controllerVars[varName]))


				for templateName in self.siteObj._templates:
					if "${" + templateName + "}" in compiledContent:
						template = self.siteObj._templates[templateName]
						templateContent = ""
						if template.TemplateFile:
							_f = open(template.TemplateFile, "r")
							templateContent = _f.read()
							_f.close()
						else:
							templateContent = template.TemplateString
						compiledContent = compiledContent.replace("${" + templateName + "}", templateContent)


				response._accepts += view.AcceptedMethods
				response.Mime = view.MimeType
				response.Content = compiledContent.encode("utf-8")
				return


			def _handle_request(self):
				requestInfo = Request(self)
				responseInfo = Response(self)
				responseInfo._isHEAD = (requestInfo.Method == "HEAD")
				responseInfo._isOPTIONS = (requestInfo.Method == "OPTIONS")
				method = requestInfo.Method
				if responseInfo._isHEAD:
					method = "GET"
				view = self.siteObj.GetView(requestInfo.Path)
				if not view:
					if self.siteObj._config.StaticServing:
						for serveAddress in self.siteObj._config.StaticFolders:
							if requestInfo.Path.startswith(serveAddress):
								localFolder = self.siteObj._config.StaticFolders[serveAddress]
								_fixedpath = requestInfo.Path.replace(serveAddress, "", 1)
								_fpath = os.path.join(localFolder, _fixedpath.lstrip("/"))
								if (os.path.exists(_fpath) and os.path.isfile(_fpath)):
									staticView = View(requestInfo.Path)
									staticView.MimeType = "text/plain"
									_fextension = os.path.splitext(_fpath)[1]
									for mimeType in MimeTypes:
										if mimeType["extension"] == _fextension:
											staticView.MimeType = mimeType["mime"]
											break
									staticView.TemplateFile = _fpath
									self.siteObj.AddView(staticView)
									self._component_handler(staticView, requestInfo, responseInfo)
									responseInfo.Send()
									return
					self._component_handler(self.siteObj._config.NotFound, requestInfo, responseInfo)
					responseInfo.Code = 404
					responseInfo.Send()
					return
				if method != "OPTIONS" and (not method in view.AcceptedMethods):
					self._component_handler(self.siteObj._config.MethodNotAllowed, requestInfo, responseInfo)
					responseInfo.Code = 405
					responseInfo.Send()
					return

				self._component_handler(view, requestInfo, responseInfo)
				responseInfo.Send()
				
				if not responseInfo.Sent:
					self._component_handler(self.siteObj._config.Error, requestInfo, responseInfo)
					responseInfo.Code = 500
					responseInfo.Send()

			protocol_version = "HTTP/2.0"
			server_version = "profess/0.1.0"

			def do_GET(self):
				self._handle_request()
			def do_HEAD(self):
				self._handle_request()
			def do_POST(self):
				self._handle_request()
			def do_PUT(self):
				self._handle_request()
			def do_DELETE(self):
				self._handle_request()
			def do_CONNECT(self):
				self._handle_request()
			def do_OPTIONS(self):
				self._handle_request()
			def do_TRACE(self):
				self._handle_request()
			def do_PATCH(self):
				self._handle_request()

		RequestHandler.siteObj = self

		self.__server = ThreadingHTTPServer(('localhost', self._config.Port), RequestHandler)

		if self._config.SSLEnabled:
			import ssl
			ssl.wrap_socket(self.__server.socket, self._config.SSLKey, self._config.SSLCertificate)

		self.__running = True
		self.__server.serve_forever()

	def Stop(self):
		if not self.__running:
			return True
		try:
			__server.shutdown()
			__server.server_close()
			self.__running = false
			return True
		except:
			raise Exception("Failed to shut active server socket down")


	def AddController(self, controller):
		types(Controller, controller)
		self.__controllers.append(controller)
		return controller

	def AddView(self, view):
		types(View, view)
		self.__views.append(view)
		return view

	def AddModel(self, model):
		types(Model, model)
		self.__models.append(model)
		return model
	def AddTemplate(self, name, template):
		types(str, name)
		types(Template, template)
		self._templates[name] = template
		return template


	def GetController(self, name):
		types(str, name)
		for controller in self.__controllers:
			if controller.Name == name:
				return controller
		return None
	def GetView(self, address):
		types(str, address)
		for view in self.__views:
			if view.WebAddress == address:
				return view
		return None
	def GetModel(self, name):
		types(str, name)
		for model in self.__models:
			if model.Name == name:
				return model
		return None


	__controllers = []
	__views = []
	__models = []
	_templates = {}
