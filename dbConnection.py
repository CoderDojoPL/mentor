import sqlite3

from flask import url_for


def connect_to_database():
    return sqlite3.connect('/database/CoderDojo.db')


def commit(conn):
    conn.commit()
    conn.close()


def rollback(conn):
    conn.rollback()
    conn.close()