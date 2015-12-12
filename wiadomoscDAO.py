import datetime
import dbConnection


def add_wiadomosc(nadawcaId, odbiorcaId, tresc):
    conn = dbConnection.connect_to_database()
    czyPrzeczytany = 0
    if conn.execute("INSERT INTO wiadomosc (NADAWCA_ID, ODBIORCA_ID, TRESC, CZY_PRZECZYTANY, DATA_WYSLANIA) "
                    "VALUES (?, ?, ?, ?, ?)", nadawcaId, odbiorcaId, tresc,
                    czyPrzeczytany, datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False

"""
:param czyPrzeczytany - integer 0/1 - ma symulowac bool'a, glupie rozwiazanie, wynika ze specyfikacji sqlite
"""


def set_wiadomosc_czy_przeczytany(wiadomoscId, czyPrzeczytany):
    conn = dbConnection.connect_to_database()
    params = (czyPrzeczytany, wiadomoscId)
    if conn.execute("UPDATE wiadomosc SET CZY_PRZECZYTANY = ? WHERE ID = ?", params):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False
