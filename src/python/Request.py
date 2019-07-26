# Request.py
# class that organizes incoming request information

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

class Request:
	Request = None

	ClientHost = None
	Path = None
	Method = None

	Headers = None
	Cookies = None

	Params = None
	Body = None
	
	def __init__(self, info):
		self.Request = info.requestline

		self.ClientHost = info.client_address[0]
		self.Path = "/" + info.path.split("?")[0].split("#")[0].lstrip("/").rstrip("/")
		self.Method = info.command
		
		self.Headers = info.headers
		
		if self.Headers["Cookie"]:
			self.Cookies = {}
			cookies = self.Headers["Cookie"].split("; ")
			for cookie in cookies:
				key = cookie.split("=")[0]
				value = cookie.split("=")[1]
				self.Cookies[key] = value

		if len(info.path.split("?")) > 1:
			self.Params = {}
			params = info.path.split("?")[1].split("#")[0]
			params = params.split("&")
			for param in params:
				key = param.split("=")[0]
				value = param.split("=")[1]
				self.Params[key] = value

		self.Body = info.rfile.read(int(self.Headers["Content-Length"] or 0))
