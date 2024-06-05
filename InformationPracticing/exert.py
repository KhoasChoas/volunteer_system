from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from functools import wraps
from flask import session, jsonify

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("admin_id") and session.get("username") and session.get('is_login'):
            return func(*args, **kwargs)
        else:
            return jsonify({
                'state': 0,
                'data': '管理员未登录'
            }), 401
    return wrapper
