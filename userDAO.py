import sqlite3


def connect_to_database():
    return sqlite3.connect('database/CoderDojo.db')


def add_user():
    conn = connect_to_database()
    conn.execute("INSERT INTO user (EMAIL, PASSWORD, LOGIN, LOKLIZACJA, CZY_USPIONY, CZY_ZDALNY, CZY_PEDAGOG) "
                 "VALUES ('adrian@a.pl', 'aa', 'aa', 'bb', '1', '1', '1' )")
    conn.commit()
    conn.close()


def does_user_exist(login, password):
    conn = connect_to_database()
    params = (login, password)
    if conn.execute("SELECT * FROM user where LOGIN = ? AND PASSWORD = ?", params):
        conn.commit()
        conn.close()
        return True
    else:
        conn.commit()
        conn.close()
        return False


def delete_user(login, password):
    conn = connect_to_database()
    if does_user_exist(login, password):
        params = (login, password)
        if conn.execute("DELETE FROM user WHERE LOGIN = ? AND PASSWORD = ?", params):
            conn.commit()
            conn.close()
            return True
        else:
            conn.rollback()
            conn.close()
            return False


add_user()
does_user_exist("aa", "aa")
delete_user("aa", "aa")
