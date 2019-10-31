from flask import Blueprint, render_template, redirect, url_for, abort, request, session
from jinja2 import TemplateNotFound
from db import mongo
from bson.objectid import ObjectId
from bs4 import BeautifulSoup

homereq = Blueprint('home', __name__)


@homereq.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        try:
            return render_template('home.html')
        except TemplateNotFound:
            abort(404)
    else:
        get_jobs = mongo.db.jobs
        jobs = get_jobs.find({})
        try:
            return render_template('home.html', all_job=jobs)
        except TemplateNotFound:
            abort(404)

# Go to post job page
@homereq.route('/home/post-job')
def go_to_post_job():
    try:
        return render_template('new-post.html')
    except TemplateNotFound:
        abort(404)

# Post a job
@homereq.route('/post-a-job', methods=['POST', 'GET'])
def post_job():
    if request.method == 'POST':
        session_email = session['email']
        salary = request.form['salary']
        duration = request.form['duration']
        title = request.form['title']
        com_name = request.form['company_name']
        job_type = request.form['job-type']
        location = request.form['location']
        description = request.form['text_editor']
        soup = BeautifulSoup(description, "html.parser").text
        if salary == "" or duration == "" or title == "" or com_name == "" or job_type == "" or location == "" or soup == "":
            try:
                return redirect(url_for('auth.error', err='Fill All the field first'))
            except TemplateNotFound:
                about(404)
        else:
            jobs = mongo.db.jobs
            jobs.insert({
                "Email": session_email,
                "Salary": salary,
                "Duration": duration,
                "Title": title,
                "Company Name": com_name,
                "Job Type": job_type,
                "Location": location,
                "Job Description": soup
            })
            try:
                return redirect(url_for('home.job_post'))
            except TemplateNotFound:
                about(404)
    else:
        try:
            return redirect(url_for('home.error', err="Fill all the field"))
        except TemplateNotFound:
            about(404)
# Go to see all jobs
@homereq.route('/home/Jobs')
def job_post():
    try:
        return render_template('job-post.html')
    except TemplateNotFound:
        abort(404)


@homereq.route('/home/Job-Details/<job_id>')
def job_detail(job_id):
    try:
        get_job = mongo.db.jobs
        jobs = get_job.find({"_id": ObjectId(job_id)})
        return render_template('job_details.html', jobs_details=jobs)
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
