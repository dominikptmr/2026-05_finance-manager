# Structure

finance-manager/
├── README.md
├── .gitignore
├── pyproject.toml
├── docs/
│   └── planning.md
├── data/
│   ├── finance_manager.db
│   │   ├── table: transactions
│   │   └── table: imports
│   └── imports/
│       └── example_transactions.csv    # example import data
├── sql/
│   └── setup.sql                       # schema for database tables
├── tests/
└── src/
    └── finance_manager/
        ├── __init__.py
        ├── main.py
        ├── models.py           # classes
        ├── csv_import.py       # read csv files
        ├── database.py         # read and write transactions to/from database, edit transaction categories
        ├── categorization.py   # categorize transactions
        ├── statistics.py       # calculate statistics from transactions and categories
        └── cli.py/gui.py       # runs cli/gui


# Pipeline

## 1. Migarate from json to db

### 1.1 Initialize SQLite database
1. Check for `finance_manager.db` and create if missing
2. Set up if does not exist (run `sql/setup.sql`)
3. Create tables if missing
    - transactions table    # Stores Transaction data
    (- imports table         # Stores import data for duplicates detection)

### 1.2 CSV import into SQLite database
.csv file -> csv_import.py -> database.py -> finance_manager.db

1. Check `/data/imports` for csv files
2. For each file:
    - Read file and extract transactions
    - Parse and clean up transaction data
    - Check if transactions are already imported (imports database table? hash? complexity for large data sets...) -> skip if already imported
    - Save transactions to `transactions` database table
    (- Save import to `imports` database table)


## 2. Migrate from csv import to API import..
- ...
