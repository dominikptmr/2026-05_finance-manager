from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

IMPORT_DIR_PATH = BASE_DIR / "data" / "imports"
STORAGE_PATH = BASE_DIR / "data" / "transactions.json"