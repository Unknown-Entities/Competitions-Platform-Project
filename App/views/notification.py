from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    notify_rank,
    handle_connect,
    send_notification,
)

notification_views = Blueprint('', __name__, template_folder='../templates')

@notification_views.route('/rankings', methods=['GET'])
@jwt_required()
def get_rankings_action():
    check = notify_rank()
    return jsonify(check), 200

@notification_views.route('/rankings/20', methods=['GET'])
@jwt_required()
def get_top_rankings_action():
    check = send_notification()
    return jsonify(check), 200
