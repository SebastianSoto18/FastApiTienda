from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#base de datos produccion
SQLALCHEMY_DATABASE_URL ="mysql+pymysql://sql10521207:gfpKq6LLHi@sql10.freemysqlhosting.net:3306/sql10521207"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
meta=MetaData()
conn = engine.connect()


#base de datos desarrollo
#SQLALCHEMY_DATABASE_URL ="mysql+pymysql://root:78945612310@localhost:3306/tienda"
#engine=create_engine(SQLALCHEMY_DATABASE_URL)
#meta=MetaData()
#conn = engine.connect()