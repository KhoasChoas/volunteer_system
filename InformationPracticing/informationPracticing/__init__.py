from flask import Flask
from flask_migrate import Migrate

from exert import db, login_manager, csrf
from LogHandler import getLogHandler
import config
from datetime import timedelta


def Create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

    # 数据库
    db.init_app(app)

    # 登录
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    # csrf
    csrf.init_app(app)

    # 日志
    file_log_handler = getLogHandler()
    app.logger.addHandler(file_log_handler)

    # 迁移
    m = Migrate(app, db)

    return app
