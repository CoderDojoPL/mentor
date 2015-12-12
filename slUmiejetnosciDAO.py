import dbConnection


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
        conn.execute("INSERT INTO sl_umiejetnosci (NAZWA) VALUE (?)", umiejetnoscNazwa)
    dbConnection.commit(conn)
