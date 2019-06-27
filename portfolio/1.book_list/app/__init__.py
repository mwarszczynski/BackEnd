import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
# from flask_bcrypt import Bcrypt
# from flask_bcrypt import *
# from flask_login import LoginManager


db = SQLAlchemy()
# bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    # with app.app_context():
    # Extensions like Flask-SQLAlchemy now know what the "current" app
    # is while within this block. Therefore, you can now run........
        # db.create_all()

    from app.users.routes import users
    from app.main.routes import main
    from app.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
