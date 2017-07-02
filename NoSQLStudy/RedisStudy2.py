import redis
conn=redis.Redis()
conn.mset({"pie":"cherry","cordial":"sherry"})
result=conn.mget(["pie","cordial"])
print(result)
conn.set("increase",1)
conn.incr("increase")
print(conn.get("increase"))
