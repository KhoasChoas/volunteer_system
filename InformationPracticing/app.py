from flask import jsonify, request, session
from flask_wtf.csrf import generate_csrf
from exert import login_manager

from informationPracticing.views import *
from informationPracticing.models import *
from informationPracticing import Create_app
from flask_cors import CORS

app = Create_app()
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})


@app.before_request
def log_each_request():
    app.logger.info('【请求方法】{}【请求路径】{}【请求地址】{}'.format(request.method, request.path, request.remote_addr))


@app.after_request
def after_request(response):
    csrf_token = generate_csrf()
    response.set_cookie('csrf_token', csrf_token)
    return response


@login_manager.user_loader
def load_user(admin_id):
    print(Admin.query.get(int(admin_id)))
    return Admin.query.get(int(admin_id))


@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({
        'state': 0,
        'data': '管理员未登录'
    }), 401


app.register_blueprint(user_blue)
app.register_blueprint(admin_blue)
app.register_blueprint(project_blue)
app.register_blueprint(root_blue)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
