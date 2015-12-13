import dbConnection


def add_user_dojo_relation(userLogin, miejscowosc):
    conn = dbConnection.connect_to_database()
    userId = conn.cursor().execute("SELECT ID FROM USER WHERE LOGIN = ?", (userLogin,)).fetchone()[0]
    dojoId = conn.cursor().execute("SELECT ID FROM dojo WHERE LOKALIZACJA = ?", (miejscowosc,)).fetchone()[0]
    params = (dojoId, userId)
    if conn.execute("INSERT INTO dojo_user VALUES (?, ?)", params):
        ilosc_mentorow = conn.execute("SELECT IL_MENTOROW FROM dojo WHERE ID = ?", dojoId)
        ilosc_mentorow += 1
        parameters = (ilosc_mentorow, dojoId)
        if conn.execute("UPDATE dojo SET IL_MENTOROW = ? WHERE ID = ?", parameters):
            dbConnection.commit(conn)
            return True
    else:
        dbConnection.rollback(conn)
        return False


def remove_user_dojo_relation(userId, dojoId):
    conn = dbConnection.connect_to_database()
    if conn.execute("DELETE FROM dojo_user WHERE USER_ID = ? AND DOJO_ID = ?", userId, dojoId):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False
