import unittest
from .. import create_app
from config import config_dict
from ..models import User
from werkzeug.security import generate_password_hash


class AuthTestCase(unittest.TestCase):

    def setUp(self):
        """
        setup the test environment
        """

        # load an instance of the flask app with tesing configurations
        self.app = create_app(config=config_dict['testing'])

        # create app context
        self.appctx = self.app.app_context()

        # bind the app context to the current context
        self.appctx.push()

        # create a test client for this app
        self.client = self.app.test_client()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def tearDown(self):
        """
        destroy the test environment
        """

        # remove the app context
        self.appctx.pop()

        self.app = None
        self.client = None

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def test_user_signup(self):
        data = {
            "username": "testuser",
            "email": "testuser@gmail.com",
            "password": 'auth123'
        }

        response = self.client.post('/api/auth/signup', json=data)

        user = User.objects(email="testuser@gmail.com").first()

        assert user.email == data['email']

        # assert response.status_code == 201

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def test_user_signin(self):
        data = {
            "email": "testuser@gmail.com",
            "password": "auth12"
        }

        response = self.client.post('/api/auth/signin', json=data)
        print(response)

        assert response.status_code == 401
