from fastapi import APIRouter, status, HTTPException
from Utils.password import verifyPassword
from Database.Models.users import Users
from Database.Models.auths import (
    LoginData,
    LoginResponse,
    TokenDataEncoded,
)
from Helper.oauth2 import create_access_token

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=LoginResponse)
def login(login_data: LoginData):
    user = Users.select().where(Users.email == login_data.email).get()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )
    if not verifyPassword(login_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )
    return LoginResponse(
        access_token=create_access_token(TokenDataEncoded(user_id=str(user.id)))
    )
