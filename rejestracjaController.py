import userDAO


def rejestruj_uzytkownika_controller(form):
    if form['password'][0] == form['passwordRepeat'][0]:
        if 'undefined' in dict(form).keys():
            del form['undefined']
        sleep = 1
        if form['registerMode'][0] == "join":
            del form['registerMode']
            sleep = 0
        login = form['login'][0]
        del form['login']
        email = form['email'][0]
        del form['email']
        password = form['password'][0]
        del form['password']
        del form['passwordRepeat']
        remote = 0
        if 'remote' in dict(form).keys():
            del form['remote']
            remote = 1
        czyPedagog = 0
        if 'experience' in dict(form).keys():
            del form['experience']
            czyPedagog = 1
        skillsTuple = ()
        for key in form:
            skillsTuple = skillsTuple + (key,)
        # miejscowosc = form[7]
        # if userDAO.add_user(login, email, password, skillsList, remote, czyPedagog, sleep, miejscowosc):
        if userDAO.add_user(login, email, password, skillsTuple, remote, czyPedagog, sleep, "Warszawa"):
            return True
    else:
        return False
