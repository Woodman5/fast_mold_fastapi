from tortoise import fields, models


class UserModel(models.Model):
    id = fields.IntField(pk=True)
    user_uuid = fields.UUIDField(index=True, unique=True, null=False)
    username = fields.CharField(index=True, unique=True, null=False, max_length=30)
    email = fields.CharField(index=True, unique=True, null=False, max_length=255)
    password = fields.CharField(null=False, max_length=255)
    is_active = fields.BooleanField(default=True, null=False)
    is_superuser = fields.BooleanField(default=False, null=False)
    is_verified = fields.BooleanField(default=False, null=False)
    first_name = fields.CharField(null=False, max_length=100)
    last_name = fields.CharField(null=False, max_length=150)
    middle_name = fields.CharField(null=True, max_length=100)
    phone = fields.CharField(null=False, max_length=15)
    address = fields.TextField(null=True)
    is_staff = fields.BooleanField(default=False, null=False)
    is_legal_person = fields.BooleanField(default=False, null=False)
    last_login = fields.DatetimeField(auto_now=True)
    date_joined = fields.DatetimeField(auto_now_add=True)

    # модель надо указать так: ключ словаря (models) как в файле main при регистрации черепахи
    # в пункте modules и далее после точки название модели которое есть в файлах,
    # перечисленных в значении (это список) этого ключа
    role = fields.relational.ForeignKeyField('models.PersonType',
                                             on_delete='CASCADE',
                                             default=4,
                                             related_name='usermodels'
                                             )

    def __str__(self):
        return self.username

    async def to_dict(self):
        d = {}
        for field in self._meta.db_fields:
            d[field] = getattr(self, field)
        for field in self._meta.backward_fk_fields:
            d[field] = await getattr(self, field).all().values()
        return d

    class Meta:
        table = 'UserAccounts_user'
        table_description = "User"


class PersonType(models.Model):
    person_type = fields.CharField(description='User type', max_length=100)
    person_slug = fields.CharField(description='Identifier', max_length=100)
    person_desc = fields.TextField(description='Description', default='', null=True)

    usermodels: fields.ReverseRelation[UserModel]

    class Meta:
        table = 'handbook_persontype'
        table_description = "User type"

    def __str__(self):
        return self.person_type
