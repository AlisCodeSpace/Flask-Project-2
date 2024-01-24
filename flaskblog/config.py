import os

class Config:
    SECRET_KEY = '7561d92f382336ab948be764f1ee5c9c'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' 

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    os.environ["EMAIL_USER"] = "utest6954@gmail.com"
    os.environ["EMAIL_PASSWORD"] = "nwcf xscy pokb fqlz"
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    