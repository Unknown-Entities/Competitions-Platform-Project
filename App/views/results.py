from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    get_user,
    is_admin,
    gather_results,
    add_results
)

result_views = Blueprint('result_views', __name__, template_folder='../templates')

@result_views.route('/results', methods=['POST'])
@jwt_required()
def add_competition_results_action():
    data = request.json
    if jwt_current_user.is_admin:
        result = add_results(userId=data['userId'], competitionId=data['competitionId'], score=data['score'])
        if result:
            return jsonify({"message": f"Result created with id {result.id}"}), 201
        return jsonify({"error": f"Either user or competition does not exist, or the result is already recorded"}), 500
    return jsonify({"error": f"User does not have authorization to add results to a competition"}), 403