from flask import current_app
from flaskblog import db

with current_app.app_context():
    db.create_all()

