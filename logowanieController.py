import userDAO


def logowanie_controller(login, password):
    return userDAO.does_user_exist(login, password)

