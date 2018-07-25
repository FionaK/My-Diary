from flask import Blueprint, Flask

app= Flask(__name__)
app.secret_key = 'fifi'

from users.views import users_blueprint
from entries.views import entries_blueprint
from route import home_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(entries_blueprint)
app.register_blueprint(home_blueprint)
