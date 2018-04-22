import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'app')))
import unittest
from main import app
from app.models import *
from sample_db import example_data
from app import connect_to_db
from flask_login import login_user, current_user
from app.routes import login, logout, register


class FlaskTestLogin(unittest.TestCase):

	def setUp(self):
		"""Do before every test"""

		# Get the Flask test client
		self.client = app.test_client()
		app.config['TESTING'] = True
		self._ctx = app.test_request_context()
		self._ctx.push()

		# Connect to test database
		connect_to_db(app, 'sqlite:////tmp/test.db')

		# Create tables and add sample data
		db.create_all()
		example_data()

	def tearDown(self):
		"""Do at end of every test"""
		if self._ctx is not None:
			self._ctx.pop()

		db.session.close()
		db.drop_all()

	"""Test login"""

	def test_login(self):
		result = login()
		self.assertIn("Log In", result)

	def test_logout(self):
		login_user(User.query.get(1))
		self.assertEquals(current_user.username, 'karen')
		self.assertFalse(current_user.is_anonymous)
		logout()
		self.assertTrue(current_user.is_anonymous)

	def test_register_page(self):
		result = register()
		self.assertIn("Sign Up", result)


if __name__ == '__main__':
	unittest.main()