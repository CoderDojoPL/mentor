# -*- coding: utf-8 -*-
import base64
import sqlite3
import urlparse
from flask import Flask, render_template, request, redirect, session, g
from uuid import uuid4
from werkzeug.debug import DebuggedApplication

DATABASE = './database/urls'
app_url = ''
app = Flask(__name__)
app.secret_key = 'M[]@#_R CI$*(_N$#*(M'

app.debug = False
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


def connect_db():
    return sqlite3.connect(DATABASE)


def encode_url(url_id):
    encoded = base64.b64encode(str(url_id))
    return 'edi.zetis.pw/matlaczm/short/' + encoded


def print_urls(db, username):
    get_urls = """SELECT * FROM urls WHERE username == '%s'""" % username
    urls = db.execute(get_urls)
    url_dict = []
    urls_name = []
    for url in urls:
        print(url[0])
        url_dict.append(encode_url(url[0]))
        urls_name.append(url[1])
    return zip(url_dict,urls_name)


@app.route(app_url + '/')
def index():
    if 'username' not in session:
        return redirect(app_url + '/login', code=302)
    username = session['username']
    data = None
    with connect_db() as db:
        data = print_urls(db,username=username)
    return render_template('login_success.html', username=username, app_url=app_url, data=data)


@app.route(app_url + '/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login_form.html', app_url=app_url)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
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
                return render_template('login_failure.html', app_url=app_url)


@app.route(app_url + '/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(app_url + '/login', code=302)



@app.route(app_url + '/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register_form.html', app_url=app_url)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with connect_db() as db:
            get_pass = """SELECT password FROM users WHERE username == '%s'""" % username
            paswd = db.execute(get_pass)
            if paswd == password:
                session['uid'] = uuid4()
                session['username'] = username
                data = print_urls(db,username=username)
                return render_template('login_success.html', username=username, app_url=app_url, data=data)
            register = """INSERT INTO users (username, password) VALUES ('%s', '%s')""" % (username, password)
            db.execute(register)
            db.commit()
        return redirect(app_url + '/login', code=302)


@app.route(app_url + '/shorten', methods=['GET', 'POST'])
def shorten():
    username = session.get('username')
    url = request.form.get('url')
    with connect_db() as db:
        insert_row = """
                INSERT INTO urls (URL, username) VALUES ('%s', '%s')
                """ % (url, username)
        try:
            cur = db.execute(insert_row)
            url_id = cur.lastrowid
            db.commit()
        except sqlite3.IntegrityError:
            get_id = """
                SELECT id FROM urls WHERE url LIKE '%s'
                """ % url
            url_id = db.execute(get_id)
            url_id = url_id.fetchone()[0]
    return render_template('shortened.html', url=encode_url(url_id), app_url=app_url)


@app.route(app_url + '/<url_shortened>')
def url_shortened_redirect(url_shortened):
    url_id = base64.b64decode(url_shortened)
    with connect_db() as db:
        get_url = """
                SELECT url FROM urls WHERE id == %d
                """ % (int(url_id))
        url = db.execute(get_url)
        url = url.fetchone()[0]
    url_scheme = urlparse.urlparse(url)
    if url_scheme[0] == '':
        url = 'http://' + url
    return redirect(url, code=302)

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
