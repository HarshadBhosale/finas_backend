from pydantic import BaseSettings


class EnvironmentVariables(BaseSettings):
    FINAS_BACKEND_ENV: str = "dev"
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    SECRET_KEY: str
    ALGORITHM: str
    TOKEN_EXPIRE_AFTER_MINS: int

    class Config:
        env_file = ".env"


envVars = EnvironmentVariables()
