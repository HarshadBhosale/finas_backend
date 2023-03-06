export DATABASE_NAME="finas"
export DATABASE_USER="harshosale"
export DATABASE_PASSWORD="harshad2000"
export DATABASE_HOST="postgres"
export DATABASE_PORT=5432

uvicorn main:api --host 0.0.0.0 --port 8888 --reload