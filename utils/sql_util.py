from sqlalchemy import Table, Column, MetaData, Integer, Computed, Identity, create_database
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy_utils import database_exists, create_database

metadata = MetaData()

def get_engine():
    engine = create_async_engine("postgresql+asyncpg://user:pass@hostname/dbname")

def initialize():
    engine = create_async_engine("postgresql+asyncpg://localhost/mydb")
    if not database_exists(engine.url):
        create_database(engine.url)

    print(database_exists(engine.url))