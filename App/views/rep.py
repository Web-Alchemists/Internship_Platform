from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from App.models import *
from.index import index_views

from App.controllers import *

rep_views = Blueprint('rep_views', __name__, template_folder='../templates')

@rep_views.route('/rep/home', methods=['GET'])
@jwt_required()
def home_page():
    return render_template('rep_home.html')

@rep_views.route('/rep/projects', methods=['GET'])
@jwt_required()
def projects_page():
    return render_template('view_projects.html', projects=projects)