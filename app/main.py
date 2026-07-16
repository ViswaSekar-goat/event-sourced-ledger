from fastapi import FastAPI

from app.db.connection import get_connection
from app.db.init_db import initialize_database

app = FastAPI()


@app.on_event("startup")
def startup():
    initialize_database()

@app.get("/")
def main():

    msg = "ledger api running"
    return msg
