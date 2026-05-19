finance-manager/
├── README.md
├── .gitignore
├── pyproject.toml
├── docs/
│   └── planning.md
├── data/
│   ├── transactions.json               # stores transaction objects
│   └── imports/
│       └── example_transactions.csv    # example import data
├── tests/
└── src/
    └── finance_manager/
        ├── __init__.py
        ├── main.py
        ├── models.py           # classes
        ├── csv_import.py       # read csv files
        ├── storage.py          # read and write transactions to/from transactions.json, edit transaction categories
        ├── categorization.py   # categorize transactions
        ├── statistics.py       # calculate statistics from transactions and categories
        └── cli.py              # runs cli


# CSV Import
.csv file -> csv_import.py -> storage.py -> transactions.json

1. Check /data/imports for csv files (pathlib)
2. For each file: Read file (csv_import.py) and check if csv file already exists in json (csv_import.py) (hash?)
    -> no: Save file's transactions in transactions.json (storage.py)
    -> yes: skip file