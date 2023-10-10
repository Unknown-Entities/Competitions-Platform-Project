from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_user, create_admin, get_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

initialize_check = False

@index_views.route('/', methods=['GET'])
def index_page():
    if initialize_check:
        print('database already initialized')
    else:
        db.drop_all()
        db.create_all()
        create_user('bob', 'bobpass', 'bob@email')
        create_admin('rob', 'robpass', 'rob@email')
        initialize_check = True
        print('database intialized')
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass', 'bob101@gmail.com')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})
