from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from App.models import *
from.index import index_views

from App.controllers import *

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/home', methods=['GET'])
def home_page():
    return render_template('admin_home.html')

@user_views.route('/students', methods=['GET'])
def view_students_page():
    return render_template('view_students.html')

@user_views.route('/students', methods=['POST'])
def view_students_page_filter():
    form_data = request.form
    return render_template('form_data_test.html', form_data=form_data)

@user_views.route('/companies', methods=['GET'])
def view_companies_page():
    return render_template('view_companies.html')

@user_views.route('/companies', methods=['POST'])
def view_companies_page_filter():
    form_data = request.form
    return render_template('form_data_test.html', form_data=form_data)

@user_views.route('/reps', methods=['GET'])
def view_reps_page():
    return render_template('view_reps.html')

@user_views.route('/reps', methods=['POST'])
def view_reps_page_filter():
    form_data = request.form
    return render_template('form_data_test.html', form_data=form_data)

@user_views.route('/projects', methods=['GET'])
def view_projects_page():
    companies = Company.query.all()
    areas = get_all_areas()
    disciplines = get_all_disciplines()
    countries = get_all_countries()
    return render_template('view_projects.html', companies=companies, areas=areas, disciplines=disciplines, countries=countries)

@user_views.route('/projects', methods=['POST'])
def view_projects_page_filter():
    form_data = request.form
    companies = Company.query.all()
    areas = get_all_areas()
    disciplines = get_all_disciplines()
    countries = get_all_countries()
    return render_template('form_data_test.html', companies=companies, areas=areas, disciplines=disciplines, countries=countries, form_data=form_data)

@user_views.route('/shortlisting', methods=['GET'])
def shortlisting_page():
    return render_template('shortlisting.html')

@user_views.route('/shortlisting', methods=['POST'])
def shortlisting_page_filter():
    form_data = request.form
    return render_template('form_data_test.html', form_data=form_data)

@user_views.route('/project/submit', methods=['GET'])
def submit_project_page():
    return render_template('project_form.html')

@user_views.route('/project/submit', methods=['POST'])
def submit_project_form_submission():
    form_data = request.form
    return render_template('form_data_test.html', form_data=form_data)

@user_views.route('/company/add', methods=['get'])
def add_company_page():
    return render_template('company_form.html')

@user_views.route('/company/add', methods=['POST'])
def add_company_form_submission():
    form_data = request.form
    return render_template('form_data_test.html', form_data=form_data)
# ----------------------------------------- #

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    user = create_user(data['username'], data['password'])
    return jsonify({'message': f"user {user.username} created with id {user.id}"})

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')