
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_date TEXT NOT NULL,
    merchant TEXT,
    description TEXT,
    amount REAL NOT NULL
);

