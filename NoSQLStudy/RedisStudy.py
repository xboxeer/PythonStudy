import redis
conn=redis.Redis()
print(conn.keys('*'))
#conn.set("secrity","hi")
print(conn.get("secrity"))
