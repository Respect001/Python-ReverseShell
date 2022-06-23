#Dasturlovchi: CLAY001
print("""  _____                                 _____ _          _ _ 
 |  __ \                               / ____| |        | | |
 | |__) |_____   _____ _ __ ___  ___  | (___ | |__   ___| | |
 |  _  // _ \ \ / / _ \ '__/ __|/ _ \  \___ \| '_ \ / _ \ | |
 | | \ \  __/\ V /  __/ |  \__ \  __/  ____) | | | |  __/ | |
 |_|  \_\___| \_/ \___|_|  |___/\___| |_____/|_| |_|\___|_|_|  """)
print("**********************Server Is Working**********************")
from socket import *

ip = "127.0.0.1"
port = 19790

connection = socket(AF_INET, SOCK_STREAM)
connection.bind((ip, port))

connection.listen(1)
client, addr = connection.accept()
print("Connect -> "+str(addr))

while True:
	recever = client.recv(1024).decode()
	print(recever)
	cmd = input("Enter your Command: ")

	if cmd == "exit":
		client.send(cmd.encode())
		exit()
	elif cmd == "" or cmd == None:
		cmd = "Error in Command"
		client.send(cmd.encode())
	elif cmd[:4] == "down":
		client.send(cmd.encode())

		data = b""
		while True:
			end_data = client.recv(1024)

			if end_data == b"Ended":
				print("END :)")
				break
			data += end_data

		file_name = input("Output file Name: ")
		new_file = open(file_name, "wb")
		new_file.write(data)
		new_file.close()

	elif cmd[:2] == "up":
		cmd_list = cmd.split(" ")

		file = cmd_list[1]
		file = open(file, "rb")
		data = file.read()
		file.close()

		client.send(cmd.encode())
		while True:
			if len(data) > 0:
				temp_data = data[0:1024]
				if len(temp_data) < 1024:
					temp_data += chr(0).encode() * (1024 - len(temp_data))

				data = data[1024:]
				client.send(temp_data)
				print("*", end="")
			else:
				client.send(b"Ended")
				print("END :)")
				break
	else:
		client.send(cmd.encode())
