import dbConnection


def add_relations(userId, umiejetnosciNames, conn):
    for name in umiejetnosciNames:
        params = (userId, name)
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
