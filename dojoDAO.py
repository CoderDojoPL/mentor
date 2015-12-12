import dbConnection


def add_dojo():
    conn = dbConnection.connect_to_database()
    params = ("Warszawa", "Warszawskie", 5)
    if conn.execute("INSERT (LOKALIZACJA, NAZWA, IL_MENTOROW) INTO dojo VALUES (?, ?, ?)", params):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False


def remove_dojo(dojoId):
    conn = dbConnection.connect_to_database()
    if conn.execute("DELETE FROM dojo WHERE ID = ?", dojoId):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False


def add_user_dojo_relation(userId, dojoId):
    conn = dbConnection.connect_to_database()
    params = (userId, dojoId)
    if conn.execute("INSERT INTO dojo_user VALUES (?, ?)", params):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False


def remove_user_dojo_relation(userId, dojoId):
    conn = dbConnection.connect_to_database()
    params = (userId, dojoId)
    if conn.execute("DELETE FROM dojo_user WHERE USER_ID = ? AND DOJO_ID = ?)", params):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False
