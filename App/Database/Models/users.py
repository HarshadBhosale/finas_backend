import peewee
from Database.Models.base_model import BaseModel as dbBaseModel
from pydantic import BaseModel, EmailStr, constr, conint
from uuid import uuid4, UUID
from datetime import datetime
from typing import Optional


class Users(dbBaseModel):
    id = peewee.UUIDField(unique=True, default=uuid4)
    name = peewee.CharField()
    email = peewee.CharField(unique=True)
    country_code = peewee.SmallIntegerField(null=True)
    mobile_number = peewee.BigIntegerField(null=True)
    password = peewee.CharField()
    access_token = peewee.CharField(unique=True, null=True)
    token_expire_at = peewee.DateTimeField(null=True)
    status = peewee.SmallIntegerField(default=1)
    created_at = peewee.DateTimeField(default=datetime.now())
    updated_at = peewee.DateTimeField(default=datetime.now())


class UserCreateModel(BaseModel):
    name: constr(min_length=1, max_length=255)
    email: EmailStr
    password: constr(min_length=8, max_length=16)
    country_code: Optional[conint(gt=0, lt=300)] = None
    mobile_number: Optional[conint(gt=999_999_999, lt=9_999_999_999)] = None

    # mobile number & country code should exist or None


class UserUpdateModel(BaseModel):
    name: Optional[constr(min_length=1, max_length=255)] = None
    password: Optional[constr(min_length=8, max_length=16)] = None
    country_code: Optional[conint(gt=0, lt=300)] = None
    mobile_number: Optional[conint(gt=999_999_999, lt=9_999_999_999)] = None

    # password update must be hashed


class UserResponseModel(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    country_code: Optional[int] = None
    mobile_number: Optional[int] = None
    access_token: Optional[str] = None
    token_expire_at: Optional[datetime] = None
    status: int
