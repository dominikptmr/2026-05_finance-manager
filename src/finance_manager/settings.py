from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

IMPORT_DIR_PATH = BASE_DIR / "data" / "imports"
STORAGE_PATH = BASE_DIR / "data" / "transactions.json"

DB_PATH = BASE_DIR / "data" / "finance_manager.db"
SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"
