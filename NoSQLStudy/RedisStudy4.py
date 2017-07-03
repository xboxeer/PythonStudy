import redis
conn=redis.Redis()
conn.hmset("song",{"do":"a deer","re":"about a deer"})
conn.hset("song","mi","a note to follow me")
print(conn.hget("song","do"))
print(conn.hgetall("song"))
print(conn.hget("song","mi"))