from database.db import engine
from sqlalchemy import inspect

def test_db_tables_exist():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert len(tables) > 0, "No tables found in database"
