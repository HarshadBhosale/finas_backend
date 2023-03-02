from pydantic import BaseModel


class RootResponseModel(BaseModel):
    API: str
