from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import initialize_db
# from app.config import Config  

app = Flask(__name__)

app.config['SECRET_KEY'] = 'wdwdqdcqwcaf3fgr'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:secret@env-db/STX'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

initialize_db(app)

from app.users.routes import users
from app.main.routes import main
from app.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(errors)


    











