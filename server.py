import socket
import json
import sys
import time
import pickle

## TODO: use pickling instead of json. pickling supports binary data

def test_functionality():
	s = socket.socket()
	print "Creating Socket\n"
	port = 12349
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(('', port))
	print "Binding socket to port",port

	running = True
	s.listen(5)
	while running:
		try:
			print "Awaiting connection request...\n"
			c, addr = s.accept()
			print 'Got connection from', addr
			size = c.recv(int(1024));
			file = c.recv(int(size)+1024);
			c.send('Connection closing...')
			c.close()
			new_object = json.loads(file)
			running = False
			return new_object
		except KeyboardInterrupt:
			running = False
	s.close()

def send_data(data, target, port):
	size = sys.getsizeof(data)
	sock = socket.socket()
	sock.connect((target, port))
	time.sleep(2)
	sock.send(str(size))
	sock.send(data)
	sock.close
	return True

def receive_data(port):
	sock = socket.socket()
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(('', port))
	sock.listen(5)
	while True:
		try:
			print "Awaiting connection request...\n"
			c, addr = sock.accept()
			print 'Got connection from', addr
			size = c.recv(int(1024));
			file = c.recv(int(size)+1024);
			c.send('Connection closing...')
			c.close()
			return file
		except KeyboardInterrupt:
			return False
	sock.close()