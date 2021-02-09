import uuid
import datetime
import ormar
from src.config.ormar_settings import database, metadata


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


# @generic_repr
# class User(AbstractBaseModel, Timestamp, SoftDelete):
#     """
#         User model
#         """
#
#     __tablename__ = "UserAccounts_User"
#
#     user_uuid = Column(UUIDType(binary=False), index=True, unique=True, nullable=False, default=uuid.uuid4())
#     username = Column(String(30), unique=True, index=True, nullable=False)
#     email = Column(EmailType, unique=True, index=True, nullable=False)
#     password = Column(String, nullable=False)
#     first_name = Column(String(150), index=True, nullable=False)
#     last_name = Column(String(150), index=True)
#     middle_name = Column(String(150), index=True)
#     phone = Column(String(30), index=True, nullable=False)
#     address = Column(String(255), index=True)
#     avatar = Column(URLType)
#     is_active = Column(Boolean, default=True)
#     is_staff = Column(Boolean, default=False)
#     is_superuser = Column(Boolean, default=False)
#     is_legal_person = Column(Boolean, default=False)
#     is_verified = Column(Boolean, default=False)
#     role_id = Column(Integer, ForeignKey('UserAccounts_Role.id'))
#     role = relationship("Role", back_populates="users")
#
#     def __str__(self):
#         return f"{type(self).__name__}(id: {self.id}, name: {self.username}"


class Role(ormar.Model):
    """
        User role model
        """

    class Meta(MainMeta):
        tablename = "useraccounts_role"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=200, unique=True, index=True, nullable=False)
    slug: str = ormar.String(max_length=200, unique=True, index=True, nullable=False)
    description: str = ormar.Text(index=True, nullable=True)
    item_removed = ormar.Boolean(default=False)
    created = ormar.DateTime(default=datetime.datetime.now, nullable=False)
    updated = ormar.DateTime(default=datetime.datetime.now, nullable=False)




