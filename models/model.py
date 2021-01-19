from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=30, unique=True, index=True, nullable=False)
    # email = Column(String(254), unique=True, index=True, nullable=False)
    #
    # password = Column(String)
    #
    # first_name = Column(String(150), index=True, default='')
    # last_name = Column(String(150), index=True, default='')
    # middle_name = Column(String(150), index=True, default='')
    # phone = Column(String(20), index=True, nullable=False)
    # address = Column(String, index=True, default='')
    #
    # is_active = Column(Boolean, default=True)
    # is_staff = Column(Boolean, default=False)
    # is_superuser = Column(Boolean, default=False)
    # is_legal_person = Column(Boolean, default=False)
    # last_login = Column(DateTime(timezone=False))
    # date_joined = Column(DateTime(timezone=False))
    #
    # role_id = Column(Integer, ForeignKey('handbook_persontype.id'))
    #
    # role = relationship("PersonType", back_populates="users")

    class Meta:
        table = "UserAccounts_user"


# class PersonType(Base):
#     __tablename__ = "handbook_persontype"
#
#     id = Column(Integer, primary_key=True, index=True)
#     person_type = Column(String(100), index=True, nullable=False)
#     person_slug = Column(String(100), index=True, nullable=False)
#     person_desc = Column(String, index=True)
#
#     users = relationship("User", back_populates="role")


