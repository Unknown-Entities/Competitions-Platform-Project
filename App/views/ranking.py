from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    get_rank,
    calculate_ranking,
    add_ranking,
    get_rankings,
    get_rankings_json
)

rank_views = Blueprint('rank_views', __name__, template_folder='../templates')

@rank_views.route('/rankings', methods=['POST'])
@jwt_required()
def add_rankings_action():
    data = request.json
    newrank = Ranking(id=id, profile_id=data['profile_id'], name=data['name'], points=data['points'], rank=data['rank'])
    db.session.add(newrank)
    db.session.commit()
    return

@rank_views.route('/rankings', methods=['GET'])
@jwt_required()
def get_rankings_action():
    return jsonify(get_rankings_json), 200
