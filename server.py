import socket
import json

s = socket.socket()
port = 12349
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', port))

running = True
s. listen(5)
while running:
	try:
		c, addr = s.accept()
		print 'Got connection from', addr
		size = c.recv(int(1024));
		file = c.recv(int(size)+1024);
		c.send('Connection closing...')
		c.close()
		new_object = json.loads(file)
		running = False
	except KeyboardInterrupt:
		running = False
s.close()
