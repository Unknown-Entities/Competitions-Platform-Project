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
def create_competion_action(id, name, category, description):
    newcomp = create_competion(id=id, name=name, category=category,  description=description)
    return create_competion

@competition_views.route('/competitions/<int:id>', methods=['POST'])
@jwt_required()
def add_competition_results_action():
    competition_id= int(request.args.get('id'))
    competition = competitions.query.get(competition_id)
    if competition is None:
        return 404
    results = request.json.get('results')
    if results is None:
        return 400
    for result in results:
        competition_result= CompetitionsResults(competition_id=competition_id,user_id=result.get('user_id'),score=result.get('score'))
        db.session.add(competition_result)
    db.session.commit()
    return jsonify({'message': 'Results added successfully.'}) 

@competition_views.route('/competitions', methods=['GET'])
@jwt_required()
def list_competitions_action():
    competitions= competitions.query.all()
    return jsonify({
        'competitions': [competition.get_json() for competition in competitions]
    })

@competition_views.route('/competitions/<int:id>', methods=['DEL'])
@jwt_required()
def delete_competition_action():
    competition_id= int(request.args.get('id'))
    competition= Competition.query.get(competition_id)
    if competition is None:
        return 404
    db.session.delete(competition)
    db.session.commit()
    return jsonify({'message': 'Competition deleted successfully.'})
    