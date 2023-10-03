from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    create_competion,
    get_competition,
    get_competion_by_name,
    get_all_competions,
    get_all_competions_json,
    edit_competions,
    update_competions,
    delete_competition
)

competition_views = Blueprint('rank_views', __name__, template_folder='../templates')

@competition_views.route('/competitions', methods=['POST'])
@jwt_required()
def create_competition_action():

@competition_views.route('/competitions/<int:id>', methods=['POST'])
@jwt_required()
def add_competition_results_action():

@competition_views.route('/competitions', methods=['GET'])
@jwt_required()
def list_competitions_action():

@competition_views.route('/competitions/<int:id>', methods=['DEL'])
@jwt_required()
def delete_competition_action():