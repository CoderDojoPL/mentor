import dbConnection
import slUmiejetnosciDAO


def add_relations(userLogin, umiejetnosciNames):
    conn = dbConnection.connect_to_database()
    userId = conn.execute("SELECT ID FROM USER WHERE LOGIN = ?", (userLogin,))
    idTuple = slUmiejetnosciDAO.get_umiejetnosc_id_tuple(umiejetnosciNames)
    for umiejetnoscId in idTuple:
        params = (userId, umiejetnoscId)
        conn.execute("INSERT INTO user_umiejetnosc VALUES (?, ?)", params)
    dbConnection.commit(conn)


def delete_users_umiejetnosci(userId):
    conn = dbConnection.connect_to_database()
    if conn.execute("DELETE FROM user_umiejetnosc where USER_ID = ?", userId):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False
