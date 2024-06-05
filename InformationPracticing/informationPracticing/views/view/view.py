from datetime import timedelta

from flask import jsonify, session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from exert import db
from informationPracticing.forms import *
from informationPracticing.models import *
from ..view import root_blue


@root_blue.route('/register', methods=['POST'])
def register():
    register_new = RegistrationForm()
    print(register_new)
    if not register_new.validate_on_submit():
        for filed_name, data in register_new.errors.items():
            return jsonify({
                'state': 0,
                'data': register_new.errors.get(filed_name)[0]
            }), 400
    try:
        username = register_new.username.data
        account = register_new.account.data
        password = register_new.password.data
        code = register_new.code.data

        admin = Admin(username=username, account=account, password=password, code=code)
        db.session.add(admin)
        db.session.commit()
        # statement = text('insert into admin(username, account, password, code) '
        #                  'values(:username, :account, :password, :code)')
        # db.session.execute(statement, username=username, account=account, password=password, code=code)
        # db.session.commit()

        return jsonify({
            'state': 0,
            'data': '注册成功'
        }), 201

    except IntegrityError as e:
        print(e)
        db.session.rollback()
        return jsonify({
            'state': 0,
            'data': '数据错误'
        }), 400
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return jsonify({
            'state': 0,
            'data': '服务器错误'
        }), 500


@root_blue.route('/login', methods=['POST'], endpoint='login')
def login():
    admin_form = LoginForm()
    if not admin_form.validate_on_submit():
        for filed_name, data in admin_form.errors.items():
            return jsonify({
                'state': 0,
                'data': admin_form.errors.get(filed_name)[0]
            }), 400
    try:
        account = admin_form.account.data
        pwd = admin_form.password.data
        admin = Admin.query.filter(Admin.account == account).first()
        if not admin.judge(account, pwd):
            return jsonify({
                'state': 0,
                'data': '密码错误',
            }), 400
        session['admin_id'] = admin.admin_id
        session['username'] = admin.username
        session['is_login'] = True
        session.permanent_session_lifetime = timedelta(days=30)
        session.permanent = True
        return jsonify({
            'state': 1,
            'data': '登录成功',
        }), 200
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return jsonify({
            'state': 0,
            'data': '服务器错误'
        }), 500
