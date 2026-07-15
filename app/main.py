from fastapi import FastAPI

from app.db.connection import get_connection

app = FastAPI()


@app.get("/")
def main():

    msg = "ledger api running"
    return msg


@app.get("/db-test")
def db_test():

    with get_connection() as conn:

        with conn.cursor() as cur:

            cur.execute("SELECT 1")

            result = cur.fetchone()

    return result