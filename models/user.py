from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine

users = Table("users", meta, 
        Column("id", Integer, primary_key=True), 
        Column("name", String(100)), 
        Column("email", String(150), unique=True), 
        Column("password", String(255)), 
        Column("phone", String(11), unique=True),
        )

meta.create_all(engine)

