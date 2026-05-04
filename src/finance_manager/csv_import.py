import csv
from modules import Transaction

def read_csv_and_create_Transaction_objects(path):
    with open(path, mode='r', newline='') as file:
        csv_file = csv.DictReader(file)
        transactions = []

        for line in csv_file:
            print(line)
            transaction = Transaction(
                date = line['date'],
                amount = line['amount'],
                description = line['description'],
                merchant = line['merchant']
            )

            transactions.append(transaction)

    return transactions