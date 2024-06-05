from flask_login import UserMixin
from sqlalchemy import UniqueConstraint
from werkzeug.security import generate_password_hash, check_password_hash

from exert import db

User_Project = db.Table(
    'user_project',
    db.Column('project_id', db.Integer, db.ForeignKey('project.project_id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'))
)


class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='管理员id')
    username = db.Column(db.String(30), unique=True, nullable=False, comment='用户名')
    account = db.Column(db.String(20), unique=True, nullable=False, comment='账号')
    password = db.Column(db.String(200), nullable=False, comment='密码（密文）')
    email = db.Column(db.String(30), comment='邮箱')
    phone = db.Column(db.String(20), comment='电话')
    sex = db.Column(db.String(10), comment='性别')
    intro = db.Column(db.String(500), comment='介绍')
    code = db.Column(db.String(200), nullable=False, comment='邀请码')

    projects = db.relationship('Project', back_populates='admin')

    def __init__(self, username, account, password, code, email=None, phone=None, sex=None, intro=None):
        self.username = username
        self.account = account
        self.pwd = password
        self.code = code
        self.email = email
        self.phone = phone
        self.sex = sex
        self.intro = intro

    def __repr__(self):
        return f'<Admin: {self.admin_id}, {self.username}>'

    def get_id(self):
        return self.admin_id

    def to_dict(self):
        return {
            'username': self.username,
            'account': self.account,
            'email': self.email,
            'phone': self.phone,
            'sex': self.sex,
            'intro': self.intro,
        }

    @property
    def pwd(self):
        return self.password

    @pwd.setter
    def pwd(self, pwd):
        self.password = generate_password_hash(pwd)

    def judge(self, account, pwd) -> bool:
        if self.account == account and check_password_hash(self.password, pwd):
            return True
        return False


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户id')
    name = db.Column(db.String(100), unique=True, nullable=False, comment='真实姓名')
    phone = db.Column(db.String(20), unique=True, nullable=False, comment='电话')
    judge = db.Column(db.Boolean, default=False, comment='是否审核')

    projects = db.relationship('Project', secondary=User_Project, back_populates='users')

    def __repr__(self):
        return f'<User: {self.user_id}, {self.name}, {self.judge}>'

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'judge': self.judge
        }


class Project(db.Model):
    __tablename__ = 'project'
    project_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='活动id')
    title = db.Column(db.String(100), unique=True, nullable=False, comment='标题')
    start_time = db.Column(db.DateTime, nullable=False, comment='开始时间')
    end_time = db.Column(db.DateTime, nullable=False, comment='结束时间')
    situation_province = db.Column(db.String(100), nullable=False, comment='地点 -- 省份')
    situation_city = db.Column(db.String(100), nullable=False, comment='地点 -- 县级市')
    require_num = db.Column(db.Integer, nullable=False, comment='活动所需人数')
    value = db.Column(db.Integer, nullable=False, comment='可获得的志愿时长')
    is_start = db.Column(db.Boolean, default=False, comment='是否已经发布')

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'), nullable=False)
    admin = db.relationship("Admin", back_populates='projects')
    users = db.relationship('User', secondary=User_Project, back_populates='projects')

    __table_args__ = (
        UniqueConstraint('start_time', 'end_time', 'situation_province', 'situation_city'),
    )

    def __repr__(self):
        return f'<Project: {self.project_id}, {self.title}>'

    def to_dict(self):
        start_time = self.start_time.strftime('%Y-%m-%d %H:%M:%S')
        end_time = self.end_time.strftime('%Y-%m-%d %H:%M:%S')
        return {
            'title': self.title,
            'start_time': start_time,
            'end_time': end_time,
            'situation_province': self.situation_province,
            'situation_city': self.situation_city,
            'require_num': self.require_num,
            'value': self.value,
            'is_start': self.is_start,
        }


class Code(db.Model):
    __tablename__ = 'code'
    invite_code = db.Column(db.String(100), primary_key=True, comment='邀请码')

    def __repr__(self):
        return f'<Code: {self.invite_code}>'
