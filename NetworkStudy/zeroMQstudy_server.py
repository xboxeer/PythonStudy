import zmq
host='127.0.0.1'
port=6789
context=zmq.Context()
server=context.socket(zmq.REP)
server.bind('tcp://%s:%s'%(host,port))
while True:
    requestByte=server.recv()
    requestStr=requestByte.decode('utf-8')
    print('the voice in my head says %s'%requestStr)
    replyStr='stop saying %s'%requestStr
    replyByts=bytes(replyStr,'utf-8')
    server.send(replyByts)

