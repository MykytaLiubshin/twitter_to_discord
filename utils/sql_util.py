from sqlalchemy import Table, Column, MetaData, Integer, Computed, Identity
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy_utils import database_exists, create_database

metadata = MetaData()

async def get_engine():
    engine = create_async_engine("postgresql+asyncpg://user:pass@hostname/dbname")

async def initialize():
    # engine = create_async_engine("postgresql+asyncpg://mykyta:hellnoboi@127.0.0.1/mydb")
    url = "postgresql+asyncpg://mykyta:hellnoboi@127.0.0.1/mydb"
    if not await database_exists(url):
        await create_database(url)

    print(database_exists(url))
