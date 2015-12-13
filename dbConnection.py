import sqlite3


def connect_to_database():
    return sqlite3.connect('database/Cfajo.db')


def commit(conn):
    conn.commit()
    conn.close()


def rollback(conn):
    conn.rollback()
    conn.close()