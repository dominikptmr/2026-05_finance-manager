import json

from settings import *

def save_transactions(transactions):
    if STORAGE_PATH.exists():
        with open(STORAGE_PATH, mode='r', encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []    
    
    for transaction in transactions:
        data.append(transaction.to_dict())

    with open(STORAGE_PATH, mode='w', encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_transactions():
    if STORAGE_PATH.exists():
        try:
            with open(STORAGE_PATH, mode='r', encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

