
from sqlalchemy import Column , Integer , String , DateTime , ForeignKey , Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine , func , DateTime
from sqlalchemy import Column,Integer,String,DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


#class User(Base_)
#	__tablename__='user'
#	__table_args__={'extend_existing':True}
#	id=Column(Integer,primary_key=True)
#	name=Column(String)
#	password=Column(String)
#	email=Column(String)
class Makeup(Base):
	__tablename__ = "makeup"
	id=Column(Integer,primary_key=True)
	picture = Column(String)
	name=Column(String)
	company=Column(String)
	description=Column(String)
	website=Column(String)






engine=create_engine('sqlite:///forum.db')
Base.metadata.create_all(engine)
Base.metadata.bind= engine
DBsession =sessionmaker(bind=engine,autoflush=False)
session =DBsession()