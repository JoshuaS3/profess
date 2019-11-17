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

import socket

class sock():
	family = socket.AF_INET
	def __init__(self):
		self.sock = socket.socket(self.family, socket.SOCK_STREAM, 0)
	def reuse_addr(self, toggle):
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, toggle and 1 or 0)
	def tcp_nodelay(self, toggle):
		self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, toggle and 1 or 0)
	def bind(self, address_tuple):
		self.sock.bind(address_tuple)
	def listen(self):
		self.sock.listen(socket.SOMAXCONN)
	def accept(self):
		return self.sock.accept()
	def close(self):
		self.sock.close()
