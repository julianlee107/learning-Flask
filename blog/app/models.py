from .__init__ import db
from werkzeug.security import generate_password_hash,check_password_hash
class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    # user属性将会返回一个根据User表中与角色表相关联的用户列表
    users=db.relationship('User',backref='role')
    # 返回一个具有可读性字符串。在测试和调试的使用
    def __repr__(self):
        return '<Role %r>' %self.name
class User(db.Model):
    __table__='users'
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    # role_id设为User的外键，与Role表联系
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'))
    def ___repr__(self):
        return '<User %r>' %self.username
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)