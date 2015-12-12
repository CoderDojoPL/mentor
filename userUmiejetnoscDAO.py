import dbConnection


def add_relations(userId, umiejetnosciIds):
    conn = dbConnection.connect_to_database()
    for id in umiejetnosciIds:
        params = (userId, id)
        if conn.execute("INSERT INTO user_umiejetnosc VALUES (?, ?)", params):
            dbConnection.commit(conn)
            return True
        else:
            dbConnection.rollback(conn)
            return False


def delete_users_umiejetnosci(userId):
    conn = dbConnection.connect_to_database()
    if conn.execute("DELETE FROM user_umiejetnosc where USER_ID = ?", userId):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False
