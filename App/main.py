from fastapi import FastAPI
from Database.database import database
from fastapi.middleware.cors import CORSMiddleware
from Database.create_tables import create_not_existence_tables
from Routers import user, auth

api = FastAPI()

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


@api.get("/")
def root():
    version = "0.1.0"
    return {"API": version}


api.include_router(user.router)
api.include_router(auth.router)
