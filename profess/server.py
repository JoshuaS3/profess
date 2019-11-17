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

from .sock import sock
from .semantics import *

class server:
	def __init__(self):
		self.sock = sock()
		self.sock.reuse_addr(True)
		self.sock.tcp_nodelay(True)
		self.sock.bind(("0.0.0.0", 8080))
		self.sock.listen()
		while True:
			connection, address = self.sock.accept()
			print("Received connection")

			request_str = connection.recv(4096).decode("latin-1")
			for line in request_str.split("\r\n"):
				print("< " + line)

			status = get_status_reason(200)
			content = "<html><body><center><h1>hello world</h1></center></body></html>"
			headers = [("content-length", len(content)), ("content-type", "text/html"), ("server", "profess/0.1.0")]

			status_str = status_line(http11, status)
			headers_str = format_headers(headers)
			response_str = full_response(status_str, headers_str, content)
			connection.sendall(response_str.encode("latin-1"))
			for line in response_str.split("\r\n"):
				print("> " + line)

			connection.close()
			print("Closing connection")
			print()
	def close():
		self.sock.close()
