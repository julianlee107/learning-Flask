import os
basedir=os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'itsaveryhardkey'
    SQLALCHMEY_COMMIT_ON_TEARDOWN=True
    FLASK_MAIL_SUBJECT_PREFIX='[Julian]'
    FLASK_MAIL_SENDER='Julian<julianlee107@vip.qq.com>'
    FLASK_ADMIN=os.environ.get('BLOG_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    MAIL_SERVER='smtp.qq.com'
    MAIL_PORT=25
    MAIL_USE_TLS=True
    MAIL_USENAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    SQLALCHMEY_DATABASE_URI=os.environ.get('DEV-DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'data-dev.sqlite')

class TestingConfig(Config):
    TESTING=True
    SQLALCHMEY_DATABASE_URI=os.environ.get('TEST-DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URO=os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'data.sqlite')

config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}