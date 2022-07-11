import time
from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)

RTTs = []
for i in range(10):
    message = f"Ping {i} {time.asctime(time.localtime())}"
    start = time.time()
    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        end = time.time()
        print(f"modifiedMessage.decode() RTT: {1000*(end - start):.2f} ms")
        RTTs.append(end-start)
    except timeout:
        print("Request timed out")
        RTTs.append(None)
clientSocket.close()

count = 0
total_rtt = 0
for RTT in RTTs:
    if RTT is not None:
        count += 1
        total_rtt += RTT
print(f"Average RTT: {total_rtt/count:.2f} ms")
print(f"Packet loss rate: {(10-count)/10*100:.2f}%")
        