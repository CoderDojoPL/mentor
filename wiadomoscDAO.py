import datetime
import dbConnection
import userDAO


def add_wiadomosc(nadawcaId, odbiorcaId, tresc, temat):
    conn = dbConnection.connect_to_database()
    czyPrzeczytany = 0
    if conn.execute("INSERT INTO wiadomosc (NADAWCA_ID, ODBIORCA_ID, TEMAT, TRESC, CZY_PRZECZYTANY, DATA_WYSLANIA) "
                    "VALUES (?, ?, ?, ?, ?, ?)", nadawcaId, odbiorcaId, temat, tresc,
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


def get_ilosc_nieprzeczytanych(odbiorcaLogin):
    odbiorcaId = userDAO.find_user_id_by_login(odbiorcaLogin)
    if odbiorcaId is not None:
        conn = dbConnection.connect_to_database()
        ilosc_nieprzeczytanych = conn.execute("SELECT COUNT(liczba) FROM wiadomosc where ODBIORCA_ID = ? AND CZY_PRZECZYTANY = 0", (odbiorcaId,))
        if ilosc_nieprzeczytanych is not None:
            return ilosc_nieprzeczytanych
    return None
