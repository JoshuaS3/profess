#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
print("TCP/IP socket created")

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("set socket options")

print("attempting to bind socket")
sock.bind(("", 8080))
print("successfully bound socket at INADDR_ANY with port 8080")

sock.listen(socket.SOMAXCONN)
print("listening")

while True:
	connection = sock.accept()
	print("new connection")
	connectionSocket = connection[0]
	connectionSource = connection[1]

	# connectionSocket.settimeout(0)

	connectionSocket.send(b"connection OK\n> ")

	fullSource = b""
	bufferString = None

	while True:
		data = connectionSocket.recv(8)
		if not data:
			break
		reply = b"received " + data + b"\n> "
		connectionSocket.sendall(reply)

	# while True:
	# 	try:
	# 		bufferString = connectionSocket.recv(4096)
	# 	except:
	# 		bufferString = None
	# 	if bufferString == None:
	# 		break
	# 	else:
	# 		print("reading buffer")
	# 		fullSource += bufferString
	# 	connectionSocket.sendall(bufferString)

	print("closing connection")
	connectionSocket.close()
