from Helper.env import envVars
from playhouse.db_url import connect

database = connect(
    f"postgresql://{envVars.DATABASE_USER}:{envVars.DATABASE_PASSWORD}@{envVars.DATABASE_HOST}:{envVars.DATABASE_PORT}/{envVars.DATABASE_NAME}"
)
