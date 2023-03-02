from fastapi import APIRouter, status, Depends
from Database.Models.users import (
    Users,
    UserCreateModel,
    UserUpdateModel,
    UserResponseModel,
)
from Database.Models.auths import LoginResponse, TokenDataEncoded
from uuid import UUID
from Helper.oauth2 import get_current_user
from Utils.password import hashPassword
from typing import Optional
from Helper.oauth2 import create_access_token
import uuid

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=Optional[list[UserResponseModel]],
)
def listAllUsers(current_user: UUID = Depends(get_current_user)):
    return list(
        Users.select()
        .where(Users.status == 1)
        .order_by(Users.created_at.desc())
        .dicts()
    )


@router.get(
    "/{id}", status_code=status.HTTP_200_OK, response_model=Optional[UserResponseModel]
)
def getUser(id: UUID, current_user: UUID = Depends(get_current_user)):
    return Users.select().where(Users.id == id, Users.status == 1).dicts().get()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponseModel)
def createUser(user: UserCreateModel):
    user.password = hashPassword(user.password)
    user = Users.create(**dict(user))
    user_id = str(uuid.UUID(int=user.id))
    token_data = TokenDataEncoded(user_id=user_id)
    token = LoginResponse(access_token=create_access_token(token_data))
    Users.update(access_token=token.access_token, token_expire_at=token_data.exp).where(
        Users.id == user_id, Users.status == 1
    ).execute()
    return (
        Users.select().where(Users.email == user.email, Users.status == 1).dicts().get()
    )


@router.put(
    "/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=UserResponseModel
)
def updateUser(
    id: UUID,
    user: UserUpdateModel,
    current_user: UUID = Depends(get_current_user),
    response_model=UserResponseModel,
):
    Users.update(user.dict(exclude_defaults=True)).where(
        Users.id == id, Users.status == 1
    ).execute()
    return Users.select().where(Users.id == id, Users.status == 1).dicts().get()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def updateUser(id: UUID, current_user: UUID = Depends(get_current_user)):
    return Users.update(status=0).where(Users.id == id, Users.status == 1).execute()
