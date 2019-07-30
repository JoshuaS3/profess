# Response.py
# class that organizes outgoing response information

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

import gzip
from .MimeTypes import *

class Response:
	Sent = False
	Code = 200
	Mime = "text/plain"
	Headers = {}
	Content = b"200 SUCCESS"

	_isHEAD = False
	_isOPTIONS = False
	_accepts = []
	_handler = None

	def __init__(self, handler):
		self.Sent = False
		self.Code = 200
		self.Mime = "text/plain"
		self.Headers = {}
		self.Content = b"200 SUCCESS"
		self._isHEAD = False
		self._isOPTIONS = False
		self._accepts = []
		self._handler = handler

	def Send(self):
		if self.Sent:
			raise Exception("Attempt to double send a response")
		
		if self._isOPTIONS or self._isHEAD:
			if self.Code == 200:
				self.Code = 204
				self.Headers["Allow"] = ", ".join(self._accepts)
				self.Headers["Access-Control-Allow-Methods"] = ", ".join(self._accepts)
		if self.Code == 405:
			if len(self._accepts) > 0:
				self.Headers["Allow"] = ", ".join(self._accepts)
		
		self._handler.send_response(self.Code)

		self.Headers["Access-Control-Allow-Origin"] = "*"
		self.Headers["Access-Control-Max-Age"] = "0"
		self.Headers["Cache-Control"] = "private, max-age=0"

		if not self._isOPTIONS:
			doGzip = True
			for mimetype in MimeTypes:
				if self.Mime == mimetype["mime"]:
					if mimetype["binary"]:
						doGzip = False
						break
			if doGzip:
				gzipped = gzip.compress(self.Content, 5)
				self.Headers["Content-Encoding"] = "gzip"
				self.Headers["Content-Length"] = len(gzipped)
			else:
				self.Headers["Content-Length"] = len(self.Content)
			self.Headers["Content-Type"] = self.Mime

		for key in self.Headers:
			value = self.Headers[key]
			self._handler.send_header(key, value)

		if not self._isHEAD and not self._isOPTIONS:
			self._handler.end_headers()
			if doGzip:
				self._handler.wfile.write(gzipped)
			else:
				self._handler.wfile.write(self.Content)
				self._handler.wfile.flush()
		else:
			self._handler.flush_headers()

		self.Sent = True
