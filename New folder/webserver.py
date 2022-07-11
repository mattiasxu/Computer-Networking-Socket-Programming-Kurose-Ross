from socket import *
import sys  # In order to terminate the program

# Prepare a sever socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept() 
    try:
        message = connectionSocket.recv(1024).decode() 
        if not message:
            connectionSocket.close()
            continue
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines() 
        connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text\html\n\n'.encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        
    except IOError:
        # Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\n\n'.encode())
        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
