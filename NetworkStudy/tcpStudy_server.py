import socket
from datetime import datetime

address=('localhost',6789)
maxSize=1024

print('starting tcp server at %s',datetime.now())
print('waiting for a client to call')
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

while True:
    client,addr=server.accept()
    data=client.recv(maxSize)
    print('at ',datetime.now(),client,' said ',data)
    client.sendall(b'are you talking to me?')
    client.close()