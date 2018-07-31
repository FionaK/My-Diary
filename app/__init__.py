from flask import Blueprint, Flask

flask_app = Flask(__name__)
flask_app.secret_key = 'fifi'

from users.views import users_blueprint
from entries.views import entries_blueprint
from route import home_blueprint

flask_app.register_blueprint(users_blueprint)
flask_app.register_blueprint(entries_blueprint)
flask_app.register_blueprint(home_blueprint)
