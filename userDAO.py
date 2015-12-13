import dbConnection
import userUmiejetnoscDAO


def add_user(status, login, email, password, passwordRepeat, skillsList, remoteExperienceList, miejscowosc):
    conn = dbConnection.connect_to_database()
    czyZdalny = 0
    czyPedagog = 0
    if status is "join":
        czyUspiony = 0
    elif status is "sleep":
        czyUspiony = 1
    else:
        return False
    if password is passwordRepeat:
        if "remote" in remoteExperienceList:
            czyZdalny = 1
        elif "experience" in remoteExperienceList:
            czyPedagog = 1
        else:
            return False
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
