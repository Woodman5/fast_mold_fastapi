import databases
import sqlalchemy

from .settings import DATABASE_URI


database = databases.Database(DATABASE_URI)

metadata = sqlalchemy.MetaData()
