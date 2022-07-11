# import socket module
from socket import *
from threading import Thread
import sys  # In order to terminate the program

def serve_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        print("Serving a client...")
        f = open(filename[1:])
        outputdata = f.readlines()
        connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text\html\n\n'.encode())
        for i in range(len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send('HTTP/1.1 404 Not Found\n\n'.encode())
        connectionSocket.close()
    except IndexError:
        connectionSocket.close()

# Prepare a server socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept() 

    thread = Thread(target=serve_client, args=(connectionSocket,))
    thread.start()
    
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
