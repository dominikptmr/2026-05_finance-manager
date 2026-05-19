import csv

from settings import *
from models import Transaction


def get_csv_files_to_import():
    csv_file_paths = []
    
    for file in IMPORT_DIR_PATH.iterdir():
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
                    amount = float(line['amount']),
                    description = line['description'],
                    merchant = line['merchant']
                    )

                transactions.append(transaction)

    return transactions

