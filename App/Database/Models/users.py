import peewee
from Database.Models.base_model import BaseModel
import pydantic


class Users(BaseModel):
    id = peewee.UUIDField(unique=True)
    name = peewee.CharField()
    email = peewee.CharField(unique=True)
    country_code = peewee.SmallIntegerField(null=True)
    mobile_number = peewee.BigIntegerField(null=True)
    password = peewee.CharField()
    access_token = peewee.CharField(unique=True)
    token_expire_at = peewee.DateTimeField()
    status = peewee.SmallIntegerField()
    created_at = peewee.DateTimeField()
    updated_at = peewee.DateTimeField()


class UserRequestModel(pydantic.BaseModel):
    pass


class UserResponseModel(pydantic.BaseModel):
    pass
