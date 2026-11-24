"""SQLite helpers with SYNTHETIC seed data only.

No real member data, ever. Every record below is fictional.
"""
import sqlite3

from flask import current_app, g

SCHEMA = """
DROP TABLE IF EXISTS claims;
CREATE TABLE claims (
    claim_id   TEXT PRIMARY KEY,
    member_id  TEXT NOT NULL,
    status     TEXT NOT NULL,
    amount_usd REAL NOT NULL
);
"""

SYNTHETIC_CLAIMS = [
    ("CLM-0001", "SYN-1001", "APPROVED", 125.00),
    ("CLM-0002", "SYN-1001", "PENDING", 980.50),
    ("CLM-0003", "SYN-1002", "DENIED", 42.10),
    ("CLM-0004", "SYN-1003", "APPROVED", 310.75),
    ("CLM-0005", "SYN-1004", "PENDING", 77.00),
]


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(_exc=None):
    conn = g.pop("db", None)
    if conn is not None:
        conn.close()


def init_db():
    conn = get_db()
    conn.executescript(SCHEMA)
    conn.executemany(
        "INSERT INTO claims (claim_id, member_id, status, amount_usd) VALUES (?, ?, ?, ?)",
        SYNTHETIC_CLAIMS,
    )
    conn.commit()


def init_app(app):
    app.teardown_appcontext(close_db)
    with app.app_context():
        init_db()
