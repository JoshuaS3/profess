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

from .types import *
from .SiteConfig import *
from .Model import *
from .View import *
from .Controller import *
from http.server import HTTPServer, BaseHTTPRequestHandler

def request(requestType, siteObj, requestObj):
	pass

class Site:
	__config = None
	__running = False
	__server = None
	__site = None

	def __init__(self, config):
		types(SiteConfig, config)
		self.__config = config
		self.__site = self

	def Start(self):
		types(SiteConfig, self.__config)
		if self.__running:
			raise Exception("Server is already running")

		class RequestHandler(BaseHTTPRequestHandler):
			def do_GET(self):
				view = None
				if not view:
					self.send_response(404)
					self.end_headers()
					self.wfile.write(b'Error 404')
					return

				self.send_response(200)
				self.end_headers()
				print(self.command)
				print(self.path)
				self.wfile.write(b'<body><h1>hello world</h1></body>')
		RequestHandler.siteObj = self

		self.__server = HTTPServer(('localhost', self.__config.Port), RequestHandler)

		if self.__config.SSL_Enabled:
			pass

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


	def GetController(self, name):
		types("str", name)
		for controller in self.__controllers:
			if controller.Name == name:
				return controller
		return None

	def GetView(self, address):
		types("str", address)
		for view in self.__views:
			if view.WebAddress == address:
				return view
		return None

	def GetModel(self, name):
		types("str", name)
		for model in self.__models:
			if model.Name == name:
				return model
		return None


	__controllers = []
	__views = []
	__models = []
