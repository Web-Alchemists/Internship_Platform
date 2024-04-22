from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from App.models import *
from.index import index_views

from App.controllers import *

student_views = Blueprint('student_views', __name__, template_folder='../templates')

@student_views.route('student/home', methods=['GET'])
def home_page():
    return render_template('student_home.html')