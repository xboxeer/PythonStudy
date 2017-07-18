import redis
conn=redis.Redis()
print('dryer is starting')
while True:
    msg=conn.blpop('dishes')
    if not msg:
        break
    val=msg[1].decode(encoding='utf-8')
    if val=='quite':
        break
    print('dried ',val)
print('Dishes are all dried')