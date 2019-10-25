from flask import Blueprint, render_template, redirect, url_for, abort, request, session
from jinja2 import TemplateNotFound
from db import mongo

authentication = Blueprint('auth', __name__)


@authentication.route("/")
def home_page():
    mongo.db.users.insert({'name': 'Tanmoy'})
    return render_template("index.html", online_users="data")