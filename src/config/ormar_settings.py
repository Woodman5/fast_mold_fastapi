import databases
import sqlalchemy

from .settings import settings


database = databases.Database(settings.database_uri)

metadata = sqlalchemy.MetaData()
