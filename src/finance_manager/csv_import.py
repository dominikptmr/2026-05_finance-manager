import csv
from pathlib import Path

from models import Transaction


def extract_transactions_from_csv_file(path):
    with open(path, mode='r', newline='') as file:
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