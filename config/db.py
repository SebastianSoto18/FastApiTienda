from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#base de datos produccion
# Creating a connection to the database.
SQLALCHEMY_DATABASE_URL ="mysql+pymysql://sql10524254:F6rxHvwcav@sql10.freemysqlhosting.net:3306/sql10524254"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()


#base de datos desarrollo
# Creating a connection to the database.
#SQLALCHEMY_DATABASE_URL ="mysql+pymysql://root:78945612310@localhost:3306/tienda"
#engine=create_engine(SQLALCHEMY_DATABASE_URL)
#sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
#Base = declarative_base()


"""
    It creates a database session, yields it to the caller, and then closes it when the caller is done
    """
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()