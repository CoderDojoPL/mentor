import userDAO


def logowanie_controller(login, password):
    if userDAO.does_user_exist(login, password):
        return True
    else:
        return False
