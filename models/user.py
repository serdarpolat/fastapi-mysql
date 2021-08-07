from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta


users = Table(
    'users',
    meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(50)),
    Column('last_name', String(50)),
    Column('email', String(50)),
    Column('password', String(255)),
)
