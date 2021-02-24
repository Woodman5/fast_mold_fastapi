import datetime
import ormar
from src.app.base.models import AbstractBaseModel, ModelMixin, SoftDeleteMixin, TimestampMixin


class Role(AbstractBaseModel, ModelMixin):
    """
        User role model
        """

    class Meta(ormar.ModelMeta):
        tablename = "useraccounts_role"


class User(AbstractBaseModel, SoftDeleteMixin, TimestampMixin):
    """
        User model
        """

    class Meta(ormar.ModelMeta):
        tablename = "useraccounts_user"

    user_uuid = ormar.UUID(uuid_format='hex', index=True, unique=True, nullable=False)
    username = ormar.String(max_length=30, unique=True, index=True, nullable=False)
    email = ormar.String(max_length=255, unique=True, index=True, nullable=False)
    password = ormar.String(max_length=255, nullable=False)
    first_name = ormar.String(max_length=150, index=True, nullable=False)
    last_name = ormar.String(max_length=150, index=True, nullable=True)
    middle_name = ormar.String(max_length=150, index=True, nullable=True)
    phone = ormar.String(max_length=30, index=True, nullable=False)
    address = ormar.String(max_length=255, index=True, nullable=True)
    avatar = ormar.String(max_length=255, nullable=True)
    is_active = ormar.Boolean(default=True)
    is_staff = ormar.Boolean(default=False)
    is_superuser = ormar.Boolean(default=False)
    is_legal_person = ormar.Boolean(default=False)
    is_verified = ormar.Boolean(default=False)
    last_login = ormar.DateTime(nullable=True)
    role = ormar.ForeignKey(Role)

    def __str__(self):
        return f"{type(self).__name__}(id: {self.id}, name: {self.username})"



