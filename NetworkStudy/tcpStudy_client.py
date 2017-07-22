import socket
from datetime import datetime
address=('localhost',6789)
maxSize=1024

print('starting client at %s'%datetime.now())
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'Hey!')
data=client.recv(maxSize)
print('at ',datetime.now,' someone replied ',data)
client.close()