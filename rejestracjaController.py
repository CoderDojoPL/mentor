import userDAO


def rejestruj_uzytkownika_controller(form):
    if form['password'][0] == form['passwordRepeat'][0]:
        sleep = 1
        if form['registerMode'][0] == "join":
            sleep = 0
        login = form['login'][0]
        email = form['email'][0]
        password = form['password'][0]
        remote = 0
        if "remo
        czyPedagog = 0
        # if len(form[6]) > 0:
        #     if "remote" in form[6]:
        #         remote  = 1
        #     if "experience" in form[6]:
        #         czyPedagog = 1
        # miejscowosc = form[7]
        # if userDAO.add_user(login, email, password, skillsList, remote, czyPedagog, sleep, miejscowosc):
        if userDAO.add_user(login, email, password, ('skill1',), remote, czyPedagog, sleep, "Warszawa"):
            return True
    else:
        return False
