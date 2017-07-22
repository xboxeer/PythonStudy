import socket
from datetime import datetime

serverAddress=('localhost',6789)
maxSize=4096

print('starting client at %s' % datetime.now())
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b'hey!',serverAddress)
data,server=client.recvfrom(maxSize)
print('At ',datetime.now(),server, ' said ',data)
client.close()
