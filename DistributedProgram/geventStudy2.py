import socket
import gevent
from gevent import monkey
monkey.patch_all()
hosts=['www.baidu.com','www.sina.com','www.amazon.cn','www.taobao.com']
jobs=[gevent.spawn(socket.gethostbyname,host) for host in hosts]
gevent.joinall(jobs,timeout=5)
for job in jobs:
    print(job.value)