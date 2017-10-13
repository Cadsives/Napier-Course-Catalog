from main import app, db
from .models import LocationPage
from .forms import LocationPageForm
from .models import CoursePage
from .forms import CoursePageForm

import flask
import flask_login

from flask import flash, redirect, request

@app.route('/admin/dashboard', methods=['GET', 'POST'])
@flask_login.login_required
def admin_dashboard():
    return flask.render_template('admin/dashboard.html')

## Adding and editing Locations
@app.route('/admin/locations', methods=['GET'])
@flask_login.login_required
def admin_locations():
    locations = LocationPage.query.all()
    return flask.render_template('admin/location-page.html',
                                locations=locations)

@app.route('/admin/locations/new', methods=['GET', 'POST'])
@flask_login.login_required
def admin_locations_new():
    form = LocationPageForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data

        page = LocationPage(name=name,
                            description=description,
                           )
        db.session.add(page)
        db.session.commit()
        return flask.redirect('/admin/locations')
    return flask.render_template('admin/location-page-edit.html',
                                form=form,
                                submit_text="Create")

@app.route('/admin/locations/<name>', methods=['GET', 'POST'])
@flask_login.login_required
def admin_locations_edit(name):
    form = LocationPageForm()
    page = LocationPage.query.filter_by(name=name).first()
    if not page:
        return flask.abort(404)
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data

        page.name = name
        page.description = description

        db.session.add(page)
        db.session.commit()
        return flask.redirect('/admin/locations')
    if request.method == 'GET':
        form.name.data = page.name
        form.description.data = page.description
    return flask.render_template('admin/location-page-edit.html',
                                form=form,
                                submit_text="Update")

## Adding and editing courses
@app.route('/admin/courses', methods=['GET'])
@flask_login.login_required
def admin_courses():
    courses = CoursePage.query.all()
    return flask.render_template('admin/course-page.html',
                                courses=courses)

@app.route('/admin/courses/new', methods=['GET', 'POST'])
@flask_login.login_required
def admin_course_new():
    form = CoursePageForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
	price = form.price.data

        page = CoursePage(name=name,
                            description=description,
				price=price,
                           )
        db.session.add(page)
        db.session.commit()
        return flask.redirect('/admin/courses')
    return flask.render_template('admin/course-page-edit.html',
                                form=form,
                                submit_text="Create")

@app.route('/admin/courses/<name>', methods=['GET', 'POST'])
@flask_login.login_required
def admin_course_edit(name):
    #print([x.key for x in CoursePage.query.all()])
    form = CoursePageForm()
    page = CoursePage.query.filter_by(name=name).first()
    if not page:
	    return flask.abort(404)
    if form.validate_on_submit():
	    name = form.name.data
	    description = form.description.data
	    price = form.price.data

	    page.name = name
	    page.description = description
	    page.price = price

	    db.session.add(page)
	    db.session.commit()
	    return flask.redirect('/admin/courses')
    if request.method == 'GET':
	    form.name.data = page.name
	    form.description.data = page.description
	    form.price.data = page.price
    return flask.render_template('admin/course-page-edit.html',
                                form=form,
                                submit_text="Update")
	 











