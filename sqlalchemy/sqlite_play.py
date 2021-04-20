#!/usr/bin/env python

import sqlalchemy
import sqlite3
from datetime import datetime

print(sqlalchemy.__version__)

conn = sqlite3.connect('database.db')
conn.execute("""
    CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        author TEXT,
        pages INTEGER,
        published INTEGER)
""")

values = ("my title", "my author", 1, datetime(2021, 5, 5).timestamp())

conn.execute("""
    INSERT INTO books VALUES (?, ?, ?, ?)
""", values)

res = conn.execute("""
    SELECT * FROM books
""")

print(res.fetchall())
