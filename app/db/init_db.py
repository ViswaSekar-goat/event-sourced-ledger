from pathlib import Path
from app.db.connection import get_connection

def initialize_database():

    schema_path = Path(__file__).parent / "schemas" / "schema.sql"

    schema_sql = schema_path.read_text()

    with get_connection() as conn:

        with conn.cursor() as cur:

            cur.execute(schema_sql)

        conn.commit()

