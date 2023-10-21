from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    generate_notification,
    notfiy,
    get_all_notifications,
    get_all_notifications,
    get_all_notifications_json
)

notification_views = Blueprint('notification_views', __name__, template_folder='../templates')

#@notification_views.route('/notfications', methods=['GET'])
#@jwt_required()
#def get_notifing_ranks_action():
#    check = notify_rank()
#    return jsonify(check), 200

@notification_views.route('/notifications', methods=['GET'])
@jwt_required()
def get_send_notification_action():
    check = send_notification(4, "Hi", False) # type: ignore
    if check:
      return jsonify({"message": f"Notification sent"}), 200
    return jsonify({"error": f"Notification sent"}), 401

@notification_views.route('/get_notfiy', method=['Get'])
def get_all_notifications():
   notif = get_all_notifications_json()
   return jsonify(notif)                 