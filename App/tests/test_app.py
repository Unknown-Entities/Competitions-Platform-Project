import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User
from App.controllers import (
    create_user,
    get_all_users_json,
    login,
    get_user,
    get_user_by_username,
    update_user
)


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    # Test for new user
    def test_new_user(self):
        user = User("bob", "bobpass", "bob@gmail.com", "1", "False")
        assert user.username == "bob"
        assert user.email == "bob@gmail.com", user.is_admin=="False"
    
    # Test for new admin user
    def test_new_admin_user(self):
        admin = User("jake", "jakepass1", "jake@gmail.com", "0", "True")
        assert admin.username == "jake"
        assert admin.email == "jake@gmail.com", admin.is_admin=="True"

    # pure function no side effects or integrations called
    def test_get_json(self):
        user = User("bob", "bobpass", "bob@gmail.com", "1", "False")
        user_json = user.get_json()
        self.assertDictEqual(user_json, {"id":None, "username":"bob"})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password, "bob@gmail.com", "1", "False")
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password, "bob@gmail.com", "1", "False")
        assert user.check_password(password)

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


def test_authenticate():
    user = create_user("bob", "bobpass", "bob@gmail.com", "1", "False")
    assert login("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "bobpass", "rick@gmail.com", "2", "False")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], users_json)

    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"
