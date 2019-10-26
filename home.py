from flask import Blueprint, render_template, redirect, url_for, abort, request, session
from jinja2 import TemplateNotFound

homereq = Blueprint('home', __name__)


@homereq.route('/home')
def home():
    return render_template('home.html')


homereq.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
