import wiadomoscDAO
import userDAO


def wyslij_wiadomosc_controller(form):
    tematWiadomosci = form[0]
    textWiadomosci = form[1]
    odbiorcaLogin = form[2]
    nadawcaLogin = form[3]
    odbiorcaId = userDAO.find_user_id_by_login(odbiorcaLogin)
    nadawcaId = userDAO.find_user_id_by_login(nadawcaLogin)
    if odbiorcaId is not None and nadawcaId is not None:
        wiadomoscDAO.add_wiadomosc(nadawcaId, odbiorcaId, textWiadomosci, tematWiadomosci)
        return True
    else:
        return False


def markuj_wiadomosc_przeczytana(form):
    wiadomoscId = form[0]
    czyPrzeczytany = 1
    if wiadomoscDAO.set_wiadomosc_czy_przeczytany(wiadomoscId, czyPrzeczytany):
        return True
    else:
        return False


def get_ilosc_nieprzeczytanych_wiadomosci(odbiorcaLogin):
    return wiadomoscDAO.get_ilosc_nieprzeczytanych(odbiorcaLogin)
