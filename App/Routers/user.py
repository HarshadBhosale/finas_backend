from fastapi import APIRouter, status, Depends
from Database.Models.users import (
    Users,
    UserCreateModel,
    UserUpdateModel,
    UserResponseModel,
)
from uuid import UUID
from Helper.oauth2 import get_current_user
from Utils.password import hashPassword

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserResponseModel])
def listAllUsers(current_user: UUID = Depends(get_current_user)):
    return list(
        Users.select()
        .where(Users.status == 1)
        .order_by(Users.created_at.desc())
        .dicts()
    )


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UserResponseModel)
def getUser(id: UUID, current_user: UUID = Depends(get_current_user)):
    return Users.select().where(Users.id == id, Users.status == 1).dicts().get()


@router.post("/", status_code=status.HTTP_201_CREATED)
def createUser(user: UserCreateModel):
    user.password = hashPassword(user.password)
    return Users.create(**dict(user))


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def updateUser(
    id: UUID, user: UserUpdateModel, current_user: UUID = Depends(get_current_user)
):
    return (
        Users.update(user.dict(exclude_defaults=True))
        .where(Users.id == id, Users.status == 1)
        .execute()
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def updateUser(id: UUID, current_user: UUID = Depends(get_current_user)):
    return Users.update(status=0).where(Users.id == id, Users.status == 1).execute()
