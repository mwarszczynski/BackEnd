import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL : True
    # MAIL_DEBUG : app.debug
    MAIL_USERNAME = 'm.warszczynski@gmail.com'
    MAIL_PASSWORD = 'testowe_haslo'
    MAIL_DEFAULT_SENDER : 'm.warszczynski@gmail.com'
