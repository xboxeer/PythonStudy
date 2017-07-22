from datetime import datetime
import socket
serverAddress=('localhost',6789)
maxSize=4096

print('Starting the server at %s' %datetime.now())
print('Waiting for a client call.')
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(serverAddress)
data, client=server.recvfrom(maxSize)

print('At ',datetime.now(),client,' said ',data)
server.sendto(b'are you talking to me?',client)
server.close()