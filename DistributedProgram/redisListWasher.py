import redis
conn=redis.Redis()
print('Washer is starting ***')
dishes=['salad','desert','entree','bread']
for dish in dishes:
    msg=dish.encode(encoding='utf_8')
    conn.rpush('dishes',msg)
    print('washed ',dish)
conn.rpush('dishes','quit')
print('all wash is done')