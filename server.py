import socket
import struct
import sys
import time
import pickle

## TODO: use pickling instead of json. pickling supports binary data

def test_functionality():
	"""
	First bit of code Steve and I (mostly Steve) wrote as a proof of concept
	"""
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

def sock_drawer():
	"""
	Returns a socket object... get it? sock drawer? ... I'll show myself out.
	"""
	return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def new_connection(sock,target,port):
	"""
	Creates a new connection
	Takes a socket object, target IP or hostname string, and port # integer
	Returns socket object 
	"""
	sock.connect((target,port))
	time.sleep(2)
	return sock

def send_data(sock, data):
	"""
	Sends one message
	Takes a data object as a bytestream, and a socket object
	Returns the socket object
	"""
	size = len(data)
	sock.sendall(struct.pack('!I',size))
	sock.sendall(data)
	return sock

def receive_data(sock, port):
	"""
	Receives one message
	Takes a socket object and a port integer to listen on
	Returns a bytestream string and the same socket object
	"""
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(('', port))
	sock.listen(5)
	while True:
		try:
			print "Awaiting connection request...\n"
			conn, addr = sock.accept()
			print 'Got connection from\n', addr
			sizebuf = recvall(conn,4); #if we start sending messages > 4GB, the number needs to be changed
			size = struct.unpack('!I',sizebuf) #creates a set with an empty element.. TODO: amend that
			data = recvall(conn, size[0]) #TODO: pass size as an int
			return data, sock
		except KeyboardInterrupt:
			return False

def recvall(conn,count):
	"""
	Credit to the Stupid Python Idea's blog for this function
	Counterpart to the sendall function.
	Takes a connection object and an integer repesenting the length of the buffer
	Returns a string representing a bytestream
	"""
	buf = b''
	while count:
		newbuf = conn.recv(count)
		if not newbuf: return None
		buf += newbuf
		count -= len(newbuf)
	return buf

def decode_image():
	pass