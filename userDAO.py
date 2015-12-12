import dbConnection


def add_user():
    conn = dbConnection.connect_to_database()
    if conn.execute("INSERT INTO user (EMAIL, PASSWORD, LOGIN, LOKLIZACJA, CZY_USPIONY, CZY_ZDALNY, CZY_PEDAGOG) "
                 "VALUES ('adrian@a.pl', 'aa', 'aa', 'bb', '1', '1', '1' )"):
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


add_user()
does_user_exist("aa", "aa")
delete_user("aa", "aa")
