import dbConnection
import sqlite3


def add_umiejetnosc(umiejetnoscNazwa):
    conn = dbConnection.connect_to_database()
    if conn.execute("INSERT INTO sl_umiejetnosci (NAZWA) VALUE (?)", umiejetnoscNazwa):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False


def remove_umiejetnosc(umiejetnoscId):
    conn = dbConnection.connect_to_database()
    if conn.execute("DELETE FROM sl_umiejetnosci WHERE ID = ?", umiejetnoscId):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False


def add_umiejetnosci(umiejetnosciNazwy):
    conn = dbConnection.connect_to_database()
    for umiejetnoscNazwa in umiejetnosciNazwy:
        conn.execute("INSERT INTO sl_umiejetnosci (NAZWA) VALUES (?)", (umiejetnoscNazwa,))
    dbConnection.commit(conn)


def get_umiejetnosc_id_tuple(umiejetnosciNazwy):
    conn = dbConnection.connect_to_database()
    id_tuple = ()
    for umiejetnoscNazwa in umiejetnosciNazwy:
        id = conn.cursor().execute("SELECT ID FROM sl_umiejetnosci WHERE NAZWA = ?", (umiejetnoscNazwa,)).fetchone()[0]
        id_tuple += (id, )
    dbConnection.commit(conn)
    return id_tuple
