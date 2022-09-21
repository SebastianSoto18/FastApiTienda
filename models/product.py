from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import meta, engine


products = Table("products",meta,
                    Column("id", Integer, primary_key=True),
                    Column("name", String(20)),
                    Column("code", String(8), unique=True),
                    Column("Quantity", Integer),    
                    Column("price", Integer)
                    )

meta.create_all(engine)