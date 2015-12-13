import userDAO


def rejestruj_uzytkownika_controller(form):
    if form[3] is form[4]:
        sleep = 1
        if form[0].value is "join":
            sleep = 0
        login = form[1]
        email = form[2]
        password = form[3]
        skillsList = form[5]
        remote = 0
        czyPedagog = 0
        if len(form[6]) > 0:
            if "remote" in form[6]:
                remote  = 1
            if "experience" in form[6]:
                czyPedagog = 1
        miejscowosc = form[7]
        if userDAO.add_user(login, email, password, skillsList, remote, czyPedagog, sleep, miejscowosc):
            return True
    else:
        return False
