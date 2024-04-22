from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies

from.index import index_views

from App.controllers import (
    login
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

def login_required(required_class):
  def wrapper(f):
      @wraps(f)
      @jwt_required()  # Ensure JWT authentication
      def decorated_function(*args, **kwargs):
        user = required_class.query.get(get_jwt_identity())
        if user.__class__ != required_class:  # Check class equality
            return jsonify(message='Invalid user role'), 403
        return f(*args, **kwargs)
      return decorated_function
  return wrapper

'''
Page/Action Routes
'''
# @auth_views.route('/users', methods=['GET'])
# def get_user_page():
#     users = get_all_users()
#     return render_template('users.html', users=users)

# @auth_views.route('/identify', methods=['GET'])
# @jwt_required()
# def identify_page():
#     return render_template('message.html', title="Identify", message=f"You are logged in as {current_user.id} - {current_user.username}")

@auth_views.route('/login', methods=['GET'])
def render_login_page():
    return render_template('login.html')

@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    token = login(data['username'], data['password'])
    response = redirect(request.referrer)
    if not token:
        flash('Bad username or password given'), 401
    else:
        flash('Login Successful')
        set_access_cookies(response, token)
        response = redirect(url_for('user_views.home_page'))
    return response

@auth_views.route('/signuptype', methods=['GET'])
def get_signup_type():
    return render_template('signup_select.html')

@auth_views.route('/signup/student', methods=['GET'])
def signup_page_student():
    role = "student"
    return render_template('signup.html',role=role)

@auth_views.route('/signup/student', methods=['POST'])
def signup_student_action():
  data = request.form  # get data from form submission
  new_user = Student(username=data['username'], password=data['password'])  # create user object
  response = None
  try:
    db.session.add(new_user)
    db.session.commit()  # save user
    token = login_user(data['username'], data['password'])
    response = redirect(url_for('student_home_page'))
    set_access_cookies(response, token)
    flash('Account Created!')  # send message
  except Exception:  # attempted to insert a duplicate user
    db.session.rollback()
    flash("username or email already exists")  # error message
    response = redirect(url_for('login_page'))
  return response

@auth_views.route('/signup/student/form', methods=['GET'])
def signup_student_form():
    return render_template('student_form.html')

@auth_views.route('/signup/student/form', methods=['POST'])
def signup_student_form_submission():
    form_data = request.form
    return render_template('form_data_test.html', form_data=form_data)

@auth_views.route('/signup/rep', methods=['GET'])
def signup_page_rep():
    role = "rep"
    return render_template('signup.html', role=role)

@auth_views.route('/signup/rep/form', methods=['GET'])
def signup_rep_form():
    return render_template('rep_form.html')

@auth_views.route('/signup/rep/form', methods=['POST'])
def signup_rep_form_submission():
    form_data = request.form
    return render_template('form_data_test.html', form_data=form_data)

@auth_views.route("/signup/rep", methods=['POST'])
def signup_action():
  response = None
  try:
    username = request.form['username']
    password = request.form['password']
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    response = redirect(url_for('rep_views.home_page'))
    token = create_access_token(identity=user)
    set_access_cookies(response, token)
  except IntegrityError:
    flash('Username already exists')
    response = redirect(url_for('signup_page'))
  flash('Account created')
  return response

@auth_views.route("/logout", methods=['GET'])
@jwt_required()
def logout_action():
  response = redirect(url_for('login_page'))
  unset_jwt_cookies(response)
  flash('Logged out')
  return response

# @auth_views.route('/logout', methods=['GET'])
# def logout_action():
#     response = redirect(request.referrer) 
#     flash("Logged Out!")
#     unset_jwt_cookies(response)
#     return response

'''
API Routes
'''

@auth_views.route('/api/login', methods=['POST'])
def user_login_api():
  data = request.json
  token = login(data['username'], data['password'])
  if not token:
    return jsonify(message='bad username or password given'), 401
  response = jsonify(access_token=token) 
  set_access_cookies(response, token)
  return response

@auth_views.route('/api/identify', methods=['GET'])
@jwt_required()
def identify_user():
    return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})

@auth_views.route('/api/logout', methods=['GET'])
def logout_api():
    response = jsonify(message="Logged Out!")
    unset_jwt_cookies(response)
    return response