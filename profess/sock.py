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

setting_family = socket.AF_INET
setting_tcp = socket.SOCK_STREAM

setting_socket_level = socket.SOL_SOCKET
setting_tcp_level = socket.IPPROTO_TCP

setting_reuse_addr = socket.SO_REUSEADDR
setting_tcp_nodelay = socket.TCP_NODELAY

max_conn = socket.SOMAXCONN

def sock(address_tuple):
	new_sock = socket.socket(setting_family, setting_tcp, 0)
	new_sock.setsockopt(setting_socket_level, setting_reuse_addr, 1)
	new_sock.setsockopt(setting_tcp_level, setting_tcp_nodelay, 1)
	new_sock.bind(address_tuple)
	return new_sock
