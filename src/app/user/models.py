import uuid

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.app.base.models import Model, AbstractBaseModel, SoftDelete
from sqlalchemy_utils import Timestamp, generic_repr, URLType, PhoneNumberType, UUIDType, EmailType, PasswordType


@generic_repr
class User(AbstractBaseModel, Timestamp, SoftDelete):
    """
        User model
        """

    __tablename__ = "UserAccounts_User"

    user_uuid = Column(UUIDType(binary=False), index=True, unique=True, nullable=False, default=uuid.uuid4())
    username = Column(String(30), unique=True, index=True, nullable=False)
    email = Column(EmailType, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String(150), index=True, nullable=False)
    last_name = Column(String(150), index=True)
    middle_name = Column(String(150), index=True)
    phone = Column(String(30), index=True, nullable=False)
    address = Column(String(255), index=True)
    avatar = Column(URLType)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_legal_person = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('UserAccounts_Role.id'))
    role = relationship("Role", back_populates="users")

    def __str__(self):
        return f"{type(self).__name__}(id: {self.id}, name: {self.username}"


class Role(AbstractBaseModel, Model):
    """
        User role model
        """

    __tablename__ = "UserAccounts_Role"

    users = relationship("User", back_populates="role")




