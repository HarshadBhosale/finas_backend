from fastapi import FastAPI, status
from Database.database import database
from fastapi.middleware.cors import CORSMiddleware
from Database.create_tables import create_not_existence_tables
from Routers import user, auth
from Database.Models.roots import RootResponseModel

api = FastAPI()
API_VERSION = "0.1.0"

origins = [
    "http://localhost:3000/",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)


@api.on_event("startup")
def startup_event():
    if database.is_closed():
        database.connect()
    create_not_existence_tables()


@api.on_event("shutdown")
def shutdown_event():
    if not database.is_closed():
        database.close()


@api.get("/", status_code=status.HTTP_200_OK, response_model=RootResponseModel)
def root():
    return RootResponseModel(API=API_VERSION)


api.include_router(user.router)
api.include_router(auth.router)
