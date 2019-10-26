import bcrypt as bcrypt
from flask import Blueprint, render_template, redirect, url_for, abort, request, session
from jinja2 import TemplateNotFound
from db import mongo

authentication = Blueprint('auth', __name__)


@authentication.route("/error/<err>")
def error(err):
    return render_template('error.html', error=err)


@authentication.route("/")
def index():
    if 'email' in session:
        try:
            return redirect(url_for('home.home'))
        except TemplateNotFound:
            abort(404)
    else:
        try:
            return render_template('index.html')
        except TemplateNotFound:
            abort(404)


@authentication.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == 'POST':
        session.pop('email', None)
        name = request.form['name']
        email = request.form['email']
        pas = request.form['pass']
        phone = request.form['num']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        pcode = request.form['pcode']
        education = request.form['edu']
        edu_inst = request.form['inst']

        if name == "" or email == "" or pas == "" or phone == "" or address == "" \
                or city == "" or state == "" or country == "" or pcode == "" or education == "" or edu_inst == "":
            try:
                return redirect(url_for('auth.index'))
            except TemplateNotFound:
                abort(404)
        else:
            users = mongo.db.users
            existing_user = users.find({"email": email})
            if existing_user is None:
                hashpass = bcrypt.hashpw(pas.encode('utf-8'), bcrypt.gensalt())
                users.insert(
                    {
                        "Name": name,
                        "Email": email,
                        "Password": hashpass,
                        "Phone number": phone,
                        "Address": address,
                        "City": city,
                        "State": state,
                        "Country": country,
                        "Postal Code": pcode,
                        "Education Level": education,
                        "Educational Institution": edu_inst
                    }
                )
                session['email'] = email
                try:
                    return redirect(url_for('home.home'))
                except TemplateNotFound:
                    abort(404)
            else:
                try:
                    return redirect(url_for('auth.error', err="Already Have an Account"))
                except TemplateNotFound:
                    abort(404)
    else:
        try:
            return redirect(url_for('auth.index'))
        except TemplateNotFound:
            abort(404)


@authentication.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.pop('email', None)
        email = request.form['email']
        pas = request.form['pass']
        if email == "" or pas == "":
            try:
                return redirect(url_for('auth.index'))
            except TemplateNotFound:
                abort(404)
        else:
            users = mongo.db.users
            username = users.find_one({'Email': email})

            if username is None:
                try:
                    return redirect(url_for('auth.error', err="invalid username or password"))
                except TemplateNotFound:
                    abort(404)
            else:
                if bcrypt.hashpw(pas.encode('utf-8'), username['Password']) == username['Password']:
                    session['email'] = email
                    try:
                        return redirect(url_for('home.home'))
                    except TemplateNotFound:
                        abort(404)
                else:
                    try:
                        return redirect(url_for('auth.error', err="invalid username or password"))
                    except TemplateNotFound:
                        abort(404)
    else:
        try:
            return redirect(url_for('auth.index'))
        except TemplateNotFound:
            abort(404)


@authentication.route('/logout')
def logout():
    session.pop('email', None)
    try:
        return redirect(url_for('auth.index'))
    except TemplateNotFound:
        abort(404)


authentication.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
