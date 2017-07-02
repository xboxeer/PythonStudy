import sqlalchemy as sa
conn=sa.create_engine('sqlite://')
print(conn.execute('''create table zoo(critter VARCHAR(20) primary KEY,count INT , damages FLOAT)'''))
ins='INSERT INTO zoo (critter,count,damages) values (?,?,?)'
conn.execute(ins,'duck',1,0.0)
conn.execute(ins,'bear',1,1000.0)
rows=conn.execute('select * from zoo')
for row in rows:
    print(row)