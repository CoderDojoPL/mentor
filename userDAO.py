import dbConnection
import userUmiejetnoscDAO


def add_user(login, email, password, skillsList, czyZdalny, czyPedagog, czyUspiony, miejscowosc):
    conn = dbConnection.connect_to_database()
    params = (email, password, login, miejscowosc, czyUspiony, czyZdalny, czyPedagog)
    if conn.execute("INSERT INTO user (EMAIL, PASSWORD, LOGIN, LOKLIZACJA, CZY_USPIONY, CZY_ZDALNY, CZY_PEDAGOG) "
                     "VALUES (?, ?, ?, ?, ?, ?, ?)", params):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False


def does_user_exist(login, password):
    conn = dbConnection.connect_to_database()
    params = (login, password)
    if conn.execute("SELECT * FROM user where LOGIN = ? AND PASSWORD = ?", params):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
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


add_user("sleep", "revenant", "adrian.michalik@wp.pl", "adrian", "adrian", ('skill1', 'skill2'), ('remote'), "Warszawa")
add_user("join", "revenantq", "adrian_michalik@wp.pl", "adrian", "adrian", ('skill1', 'skill2'), ('experience'), "Warszawa")
