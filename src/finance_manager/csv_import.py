import csv, json
from pathlib import Path

from models import Transaction

storage_path = Path('finance-manager/data/transactions.json')
imports_dir_path = Path('finance-manager/data/imports')

BASE_DIR = Path(__file__).resolve().parent.parent.parent

imports_dir_path = BASE_DIR / "data" / "imports"
storage_path = BASE_DIR / "data" / "transactions.json"


def get_csv_files_to_import():
    csv_file_paths = []
    
    for file in imports_dir_path.iterdir():
        if file.suffix == '.csv':
            csv_file_paths.append(file)
    
    return csv_file_paths


def extract_transactions_from_csv_files(csv_file_paths):
    
    transactions = []
    
    for path in csv_file_paths:
        with open(path, mode='r', newline='') as file:
            csv_file = csv.DictReader(file)

            for line in csv_file:
                transaction = Transaction(
                    date = line['date'],
                    amount = line['amount'],
                    description = line['description'],
                    merchant = line['merchant']
                    )

                transactions.append(transaction)

    return transactions


def save_transactions_to_json(transactions):
    with open(storage_path, mode='r', encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
        
    for transaction in transactions:
        data.append(transaction.to_dict())

    with open(storage_path, mode='w', encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def import_csv_files():
    save_transactions_to_json(extract_transactions_from_csv_files(get_csv_files_to_import()))