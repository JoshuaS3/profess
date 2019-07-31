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

from .sock import sock, max_conn
from .semantics import *

class server:
	def __init__(self):
		self.sock = sock(("0.0.0.0", 8080))
		self.sock.listen(max_conn)
		while True:
			connection, address = self.sock.accept()
			status = get_status_reason(200)
			content = "<html><body><h1>tesaaaaaat</h1></body></html>"
			headers = [("content-length", len(content)), ("content-type", "text/html"), ("server", "profess/0.1.0")]

			status_str = status_line(http20, status)
			headers_str = format_headers(headers)
			connection.sendall(full_response(status_str, headers_str, content).encode("utf-8"))
			connection.close()
			print("> " + status_str)
