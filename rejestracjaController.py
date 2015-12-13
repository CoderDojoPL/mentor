import userDAO


def rejestruj_uzytkownika_controller(form):
    if form['password'][0] == form['passwordRepeat'][0]:
        if 'undefined' in dict(form).keys():
            del form['undefined']
        sleep = 1
        if form['registerMode'][0] == "join":
            sleep = 0
        del form['registerMode']
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
        miejscowosc = form['location']
        del form['location']
        skillsTuple = ()
        for key in form:
            skillsTuple = skillsTuple + (key,)
        # if userDAO.add_user(login, email, password, skillsList, remote, czyPedagog, sleep, miejscowosc):
        if userDAO.add_user(login, email, password, skillsTuple, remote, czyPedagog, sleep, miejscowosc):
            return True
    else:
        return False
