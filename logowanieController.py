import userDAO


def logowanie_controller(form):
    login = form[0]
    password = form[1]
    if userDAO.does_user_exist(login, password):
        return True
    else:
        return False
