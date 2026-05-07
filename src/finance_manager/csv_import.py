import csv, json
from pathlib import Path

from models import Transaction

storage_path = Path('finance-manager/data/transactions.json')
imports_dir_path = Path('finance-manager/data/imports')


def get_csv_files_to_import():
    csv_file_paths = []
    
    for file in imports_dir_path.iterdir():
        if file.suffix == '.csv':
            csv_file_paths.append(str(file))
    
    return csv_file_paths


def extract_transactions_from_csv_file(csv_file_path):
    with open(csv_file_path, mode='r', newline='') as file:
        csv_file = csv.DictReader(file)

        transactions = []

        for line in csv_file:
            transaction = Transaction(
                date = line['date'],
                amount = line['amount'],
                description = line['description'],
                merchant = line['merchant']
                )

            transactions.append(transaction)

    return transactions

