def dryer():
    import redis
    import os
    import time
    conn=redis.Redis()
    pid=os.getpid()
    timeout=5
    print('dryer process %s is starting' % pid)
    while True:
        msg=conn.blpop('dishes')
        if not msg:
            break
        val=msg[1].decode(encoding='utf-8')
        if val=='quit':
            break
        print('%s dried %s' %(pid,val))
        time.sleep(0.1)

import multiprocessing
for num in range(3):
    process=multiprocessing.Process(target=dryer)
    process.start()
