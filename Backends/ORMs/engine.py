#!/usr/bin/python

from sqlalchemy import create_engine

# DB_Url = f'mysql://user:password@host:port/database'
# engine = create_engine(DB_Url)
engine = create_engine('Mysql://scott:tiger@localhost/foo')

with engine.connect() as connection:
    result = connection.execute("Select username from users")
    for row in result:
        print("username:", row['username'])

with engine.connect() as connecton:
    with connection.begin()
        r1 = connection.execute(table1.select())
        connection.execute(table1.insert(), {"col1": 7, "col2": "This is some data"})


def method_a(connection):
    with connection.begin():
        method_b(connection)

def method_b(conncetion):
    with connection.begin():
        connection.execute("insert into mytable values ('bat', 'lala')")
        connection.execute(mytable.insert(), {"col1": "bat", "col2": "lala"})

# metadata
# 
fom sqlalchemy import MetaData, Table, Column, Integer

meta = MetaData()
users_table = Table('users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(50))
)
