import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
conn=sa.create_engine('sqlite:///zoo.db')
base=declarative_base()
class zoo(base):
    __tablename__='zoo'
    critter=sa.Column('critter',sa.String,primary_key=True)
    count=sa.Column('count',sa.Integer)
    damages=sa.Column('damage',sa.Float)
    def __init__(self,critter,count,damages):
        self.critter=critter
        self.count=count
        self.damages=damages
    def __repr__(self):
        return '<Zoo ({},{},{})>'.format(self.critter,self.count,self.damages)
base.metadata.create_all(conn)
first=zoo('duck',1,1.0)
second=zoo('bear',1,1000.0)
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(bind=conn)
session=Session()
session.add_all([first,second])
session.commit()


