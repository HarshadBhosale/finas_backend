import peewee
from Database.Models.base_model import BaseModel
import pydantic
import playhouse.postgres_ext


class Logs(BaseModel):
    id = peewee.UUIDField(unique=True)
    message = peewee.CharField(null=True)
    function = peewee.CharField(null=True)
    params = playhouse.postgres_ext.BinaryJSONField(null=True)
    status = peewee.SmallIntegerField()
    created_at = peewee.DateTimeField()
    updated_at = peewee.DateTimeField()


class LogRequestModel(pydantic.BaseModel):
    pass


class LogResponseModel(pydantic.BaseModel):
    pass
