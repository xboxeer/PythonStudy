import redis
conn=redis.Redis()
result=conn.lpush("zoo","duck")
print(result)
result=conn.lpush("zoo","bear","tiger")