# -*- coding: utf-8 -*-
import sqlite3
from flask import Flask, render_template, request, redirect, session, g
from uuid import uuid4
from werkzeug.debug import DebuggedApplication
import rejestracjaController
import logowanieController


DATABASE = './database/urls'
app_url = ''
app = Flask(__name__)
app.secret_key = 'M[]@#_R CI$*(_N$#*(M'
app.debug = True

app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route(app_url + '/')
def index():
    if 'username' not in session:
        return redirect(app_url + '/login', code=302)
    username = session['username']
    return render_template('login_success.html', username=username, app_url=app_url)


@app.route(app_url + '/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html', app_url = app_url)
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if logowanieController.logowanie_controller(login, password):

        with connect_db() as db:
            get_pass = """SELECT password FROM users WHERE username == '%s'""" % username
            passwd = db.execute(get_pass)
            try:
                if passwd.fetchone()[0] == password:
                    session['uid'] = uuid4()
                    session['username'] = username
                    data = print_urls(db,username=username)
                    return render_template('login_success.html', username=username, app_url=app_url, data=data)
            except TypeError:
                return render_template('login.html', app_url=app_url)


@app.route(app_url + '/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(app_url + '/login', code=302)



@app.route(app_url + '/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register_form.html', app_url=app_url)
    if request.method == 'POST':
        read = dict(request.form)
        rejestracjaController.rejestruj_uzytkownika_controller(read)
        return redirect(app_url + '/login', code=302)


@app.route(app_url + '/messages', methods=['GET', 'POST'])
def messages():
    messages = []
    messages.append({'title':'first message','content':'this is content','button':'http://google.pl'})
    for message in messages:
        print(message['title'])
    return render_template('messages.html', messages=messages)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

    # http://0.0.0.0:4000/matlaczm/urlShortener/login
