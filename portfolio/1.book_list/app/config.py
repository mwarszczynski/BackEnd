import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# class Config:
#     app.config['SECRET_KEY'] = 'wdwdqdcqwcaf3fgr'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:secret@env-db/STX'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False