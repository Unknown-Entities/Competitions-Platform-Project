from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required
from App.models import Competition

from .index import index_views

from App.controllers import (
    get_user,
    is_admin,
    create_competion,
    get_competition,
    get_competion_by_name,
    get_all_competions,
    get_all_competions_json,
    edit_competions,
    gather_results,
    update_competions,
    delete_competition
)

competition_views = Blueprint('competition_views', __name__, template_folder='../templates')

@competition_views.route('/competitions', methods=['POST'])
@jwt_required()
def create_competition_action():
    data = request.json
    if jwt_current_user.is_admin:
        comp = create_competion(name=data['name'], category=data['category'], description=data['description'])
        if comp:
            return jsonify({"message": f"Competition created with id {comp.id}"}), 201
        return jsonify({"error": f"Competition {data['name']} already exists "}), 500
    return jsonify({"error": f"User does not have authorization to create a competition"}), 403

@competition_views.route('/competitions', methods=['GET'])
@jwt_required()
def list_competitions_action():
    competitions = get_all_competions_json()
    return jsonify(competitions), 200

@competition_views.route('/competitions/<int:id>', methods=['GET'])
@jwt_required()
def competition_details_action(id):
    competition = Competition.query.get(id)
    if competition:
        comp_results = gather_results(id)
        return jsonify(competition.get_json(), comp_results), 200
    return jsonify({"error": f"Competition does not exist"}), 500

@competition_views.route('/competitions/<int:id>', methods=['DEL'])
@jwt_required()
def delete_competition_action():
    return
    