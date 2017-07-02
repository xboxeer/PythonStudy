import sqlalchemy as sa
conn=sa.create_engine('sqlite://')
meta=sa.MetaData()
zoo=sa.Table('zoo',meta,\
sa.Column('critter',sa.String,primary_key=True),\
sa.Column('count',sa.Integer),\
sa.Column('damages',sa.Float))
meta.create_all(conn)
conn.execute(zoo.insert(('duck',1,1.0)))
conn.execute(zoo.insert(('bear',1,1000.0)))
result=conn.execute(zoo.select())
rows=result.fetchall()
print(rows)