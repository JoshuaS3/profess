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

class Response:
	Sent = False
	Code = 200
	Mime = "text/plain"
	Headers = {}
	Content = "200 SUCCESS"

	_isHEAD = False
	_handler = None

	def __init__(self, handler):
		self._handler = handler

	def Send(self):
		if self.Sent:
			raise Exception("Attempt to double send a response")
		self._handler.send_response(self.Code)
		self.Headers["Content-Length"] = len(self.Content)
		self.Headers["Content-Type"] = self.Mime
		for key in self.Headers:
			value = self.Headers[key]
			self._handler.send_header(key, value)
		if not self._isHEAD:
			self._handler.end_headers()
			self._handler.wfile.write(self.Content)
		self.Sent = True
