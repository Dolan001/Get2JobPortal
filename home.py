from flask import Blueprint, render_template, redirect, url_for, abort, request, session
from jinja2 import TemplateNotFound

homereq = Blueprint('home', __name__)


@homereq.route('/home')
def home():
    try:
        return render_template('home.html')
    except TemplateNotFound:
        abort(404)


@homereq.route('/home/post-job')
def go_to_post_job():
    try:
        return render_template('new-post.html')
    except TemplateNotFound:
        abort(404)


@homereq.route('/home/Jobs')
def job_post():
    try:
        return render_template('job-post.html')
    except TemplateNotFound:
        abort(404)


@homereq.route('/home/Job-Details')
def job_detail():
    try:
        return render_template('blog-single.html')
    except TemplateNotFound:
        abort(404)


@homereq.route('/home/contact')
def contact():
    try:
        return render_template('contact.html')
    except TemplateNotFound:
        abort(404)


@homereq.route('/home/blog')
def blog():
    try:
        return render_template('blog.html')
    except TemplateNotFound:
        abort(404)


@homereq.route('/home/blog-details')
def blog_details():
    try:
        return render_template('blog-single.html')
    except TemplateNotFound:
        abort(404)


@homereq.route('/home/about')
def about():
    try:
        return render_template('blog-single.html')
    except TemplateNotFound:
        abort(404)


homereq.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
