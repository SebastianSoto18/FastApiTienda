from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta, engine

users = Table("users", meta, 
        Column("id", Integer, primary_key=True), 
        Column("name", String(100)), 
        Column("email", String(150)), 
        Column("password", String(50)), 
        Column("phone", String(11)))

meta.create_all(engine)

