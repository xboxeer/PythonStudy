import gevent
from gevent import socket
hosts=['www.baidu.com','www.sina.com','www.taobao.com']
jobs=[gevent.spawn(gevent.socket.gethostbyname,host) for host in hosts ]
gevent.joinall(jobs,timeout=5)
for job in jobs:
    print(job.value)