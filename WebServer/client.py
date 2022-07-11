from socket import *
import sys

if len(sys.argv) != 4:
    print("Usage: python3 client.py <server_ip> <server_port> <file_name>")

serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

request = "GET " + filename + " HTTP/1.1\r\n\r\n"

clientSocket.send(request.decode())
response = clientSocket.recv(1024).decode()
while response:
    print(response.decode())
    response = clientSocket.recv(1024).decode()
clientSocket.close()