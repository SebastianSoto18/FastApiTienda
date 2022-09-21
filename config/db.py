from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL ="postgresql+psycopg2://edzllzmzvihoqx:dc26badfb8c20013711be5db25a7135b8e8ed5fb82cc24d6ca3c8be5dec44160@ec2-34-231-42-166.compute-1.amazonaws.com:5432/d8ulfv2ruqif38"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
meta=MetaData()
conn = engine.connect()