from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_user, create_admin

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    check = get_user(2)
    if check:
        print('database already initialized')
    else:
        db.drop_all()
        db.create_all()
        create_user('bob', 'bobpass', 'bob@email')
        create_admin('rob', 'robpass', 'rob@email')
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
