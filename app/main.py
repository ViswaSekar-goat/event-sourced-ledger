from fastapi import FastAPI
import app.domain.account_events as EventManager
from app.db.connection import get_connection
from app.db.init_db import initialize_database
import uuid
from app.db.event_store import EventStore as Event

app = FastAPI()


@app.on_event("startup")
def startup():
    initialize_database()

@app.get("/")
def main():

    msg = "ledger api running"
    random_uuid = uuid.uuid4()
    account_deposit = EventManager.Deposited(random_uuid,1,500)
    account_withdraw = EventManager.Withdrawn(random_uuid,2,500)
    store = Event()
    store.append_event(account_deposit)
    store.append_event(account_withdraw)
    return msg
