import dbConnection
import userUmiejetnoscDAO
import dojoUserDAO


def add_user(login, email, password, skillsList, czyZdalny, czyPedagog, czyUspiony, miejscowosc):
    conn = dbConnection.connect_to_database()
    params = (email, password, login, miejscowosc[0], czyUspiony, czyZdalny, czyPedagog)
    if conn.execute("INSERT INTO user (EMAIL, PASSWORD, LOGIN, LOKALIZACJA, CZY_USPIONY, CZY_ZDALNY, CZY_PEDAGOG) "
                     "VALUES (?, ?, ?, ?, ?, ?, ?)", params):
        dbConnection.commit(conn)
        userUmiejetnoscDAO.add_relations(login, skillsList)
        return True
    else:
        dbConnection.rollback(conn)
        return False


def does_user_exist(login, password):
    conn = dbConnection.connect_to_database()
    if (login,) in conn.cursor().execute("SELECT LOGIN FROM user").fetchall():
        if password == conn.execute("SELECT PASSWORD FROM user where LOGIN = ?", (login,)).fetchone()[0]:
            return True
        else:
            return False


def delete_user(login, password):
    conn = dbConnection.connect_to_database()
    if does_user_exist(login, password):
        params = (login, password)
        if conn.execute("DELETE FROM user WHERE LOGIN = ? AND PASSWORD = ?", params):
            dbConnection.commit(conn)
            return True
        else:
            dbConnection.rollback(conn)
            return False


def find_user_id_by_login(login):
    conn = dbConnection.connect_to_database()
    id = conn.cursor().execute("SELECT id FROM user where LOGIN = ? AND PASSWORD = ?", (login,)).fetchone()[0]
    if id is not None:
        dbConnection.commit(conn)
        return id
    else:
        dbConnection.rollback(conn)
        return None


def find_inactive_users():
    conn = dbConnection.connect_to_database()
    inactive_users = conn.cursor().execute("SELECT LOGIN, LOKALIZACJA FROM user WHERE CZY_USPIONY = 1").fetchall()
    dbConnection.commit(conn)
    return inactive_users


def find_active_users():
    conn = dbConnection.connect_to_database()
    inactive_users = conn.cursor().execute("SELECT LOGIN, LOKALIZACJA FROM user WHERE CZY_USPIONY = 0").fetchall()
    dbConnection.commit(conn)
    return inactive_users


def find_miejscowosci_and_liczba_usbionych():
    conn = dbConnection.connect_to_database()
    idList = conn.cursor().execute("SELECT ID FROM user").fetchall()
    lista_slownikow = ()
    for id in idList:
        miejscowosc = conn.cursor().execute("SELECT LOKALIZACJA FROM user WHERE ID = ?", (id[0],)).fetchone()[0]
        liczba_uspionych = conn.cursor().execute("SELECT COUNT(ID) FROM user WHERE LOKALIZACJA = ? AND CZY_USPIONY = 1", (miejscowosc,)).fetchone()[0]
        slownik = {'Miejscowosc': miejscowosc, 'Liczba_uspionych': liczba_uspionych}
        lista_slownikow = lista_slownikow + (slownik,)
    return lista_slownikow

find_miejscowosci_and_liczba_usbionych()