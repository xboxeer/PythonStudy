import redis
days=["2017-01-01","2017-01-02","2017-01-03"]
bigSpender=1089
trieKicker=40459
lateJoiner=550212
conn=redis.Redis()
conn.setbit(days[0],bigSpender,1)
conn.setbit(days[0],trieKicker,1)
conn.setbit(days[1],bigSpender,1)
conn.setbit(days[2],bigSpender,1)
conn.setbit(days[2],lateJoiner,1)
for day in days:
    visitCount=conn.bitcount(day)
    print(visitCount)
print(conn.getbit(days[0],bigSpender))
#这里 and 操作是将days[0], days[1],days[2]三个bitmap取
#比如days[0]=110,days[1]=100，days[2]=101，那么在days取and的结果就是100，因为只有中间一位在days[0],days[1],days[2]
#里面都是1
print(conn.bitop("and","everyday",*days))
print(conn.bitcount("everyday"))
print(conn.bitop("or","alldays",*days))
print(conn.bitcount("alldays"))
print(conn.getbit("alldays",bigSpender))
print(conn.getbit("alldays",lateJoiner))