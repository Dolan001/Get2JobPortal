from flask import Blueprint, render_template, redirect, url_for, abort, request, session
from jinja2 import TemplateNotFound

homereq = Blueprint('home', __name__)
