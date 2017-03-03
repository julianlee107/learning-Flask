import os

basedir=os.path.abspath(os.path.dirname(__file__))
# 存储数据库文件路径
SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'app.db')
# 讲SQLAlchemy-migrate数据文件存储在这个文件夹中
SQLALCHEMY_MIGRATE_REPO=os.path.join(basedir,'db_repository')

# web表单验证
CSRF_ENABLE=True
SECRET_KEY='CANYOUGuEssMe?'