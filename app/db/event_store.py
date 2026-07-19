from app.db.connection import get_connection
from psycopg.types.json import Json
from pathlib import Path

class EventStore:

    def __init__(self):
        self._append_schema_path = Path(__file__).parent / "schemas" / "append.sql"
        self._append_schema_sql = self._append_schema_path.read_text()

    def append_event(self, event):
        
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(self._append_schema_sql,
                    (
                        event.stream_id,
                        event.stream_version,
                        event.event_type,
                        Json(event.to_payload()),
                        event.created_at
                    )
                )

            conn.commit()


    def load_events(self, stream_id):
        pass