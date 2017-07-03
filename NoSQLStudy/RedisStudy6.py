import redis
import time
now=time.time()
conn=redis.Redis()
conn.zadd("logins","elendil",now)
conn.zadd("logins","elendil2",now+60)