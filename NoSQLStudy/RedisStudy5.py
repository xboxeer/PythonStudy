import redis
conn=redis.Redis()
conn.delete("zoo")
conn.sadd("zoo","duck","bear")
print(conn.scard("zoo"))
print(conn.smembers("zoo"))
conn.sadd("betterZoo","tiger","duck")
print(conn.sdiff("betterZoo","zoo"))
print(conn.sinter("zoo","betterZoo"))