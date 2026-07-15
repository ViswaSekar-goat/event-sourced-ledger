from fastapi import FastAPI

app = FastAPI(title="Event Sourced Ledger")


@app.get("/")
def root():
    return {
        "message": "Ledger API is running"
    }