import unittest
from .. import create_app
from config import config_dict
from ..models import User


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
