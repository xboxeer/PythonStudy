import zmq
host='127.0.0.1'
port=6789
context=zmq.Context()
client=context.socket(zmq.REQ)
client.connect("tcp://%s:%s"%(host,port))
for num in range(6):
    requestStr='message %s'%num
    requestBytes=requestStr.encode(encoding='utf_8')
    client.send(requestBytes)
    replyBytes=client.recv()
    replyStr=replyBytes.decode('utf-8')
    print('send %s, receive %s'%(requestStr,replyStr))