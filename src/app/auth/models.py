import ormar
from src.config.ormar_settings import database, metadata
from src.app.user.models import User


class Verification(ormar.Model):
    """ Модель для подтверждения регистрации пользователя """

    class Meta:
        abstract = True
        metadata = metadata
        database = database

    link = ormar.UUID(primary_key=True)
    user = ormar.ForeignKey(User)
