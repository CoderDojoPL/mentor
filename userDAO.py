import dbConnection
import userUmiejetnoscDAO


def add_user(login, email, password, skillsList, czyZdalny, czyPedagog, czyUspiony, miejscowosc):
    conn = dbConnection.connect_to_database()
    params = (email, password, login, miejscowosc, czyUspiony, czyZdalny, czyPedagog)
    if conn.execute("INSERT INTO user (EMAIL, PASSWORD, LOGIN, LOKALIZACJA, CZY_USPIONY, CZY_ZDALNY, CZY_PEDAGOG) "
                     "VALUES (?, ?, ?, ?, ?, ?, ?)", params):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False


def does_user_exist(login, password):
    conn = dbConnection.connect_to_database()
    if (login,) in conn.execute("SELECT LOGIN FROM user").fetchall():
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
    id = conn.execute("SELECT id FROM user where LOGIN = ? AND PASSWORD = ?", (login,))
    if id is not None:
        dbConnection.commit(conn)
        return id
    else:
        dbConnection.rollback(conn)
        return None

does_user_exist("asda", "asgsfa")