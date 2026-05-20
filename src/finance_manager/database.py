import sqlite3

from settings import *
from models import Transaction


def setup_schema():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    schema = SCHEMA_PATH.read_text()

    cursor.executescript(schema)

    connection.commit()
    connection.close()


def save_transactions(transactions):
    
    transaction_list = []
    
    for transaction in transactions:
        transaction_list.append((
            transaction.transaction_date,
            transaction.merchant,
            transaction.description,
            transaction.amount,
        ))
    
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    
    cursor.executemany("""
    INSERT INTO transactions (
        transaction_date,
        merchant,
        description,
        amount
    )
    VALUES(?, ?, ?, ?)
    """, transaction_list
    )
    
    connection.commit()
    connection.close()
    

def load_transactions():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    
    cursor.execute("""
    SELECT
        id,
        transaction_date,
        merchant,
        description,
        amount
    FROM transactions           
    """)
    
    transactions = cursor.fetchall()
    
    transaction_objects = []
    
    for transaction in transactions:
        transaction_objects.append(
            Transaction(
                id = transaction[0],
                transaction_date = transaction[1],
                merchant = transaction[2],
                description = transaction[3],
                amount = transaction[4],
            )
        )
        
    connection.close()

    return transaction_objects