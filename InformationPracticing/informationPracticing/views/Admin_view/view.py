from flask import jsonify, request

from informationPracticing.models.model import Admin
from ..Admin_view import admin_blue

import json

@admin_blue.route('/', methods=['GET'])
def get_admin():
    result = Admin.query.filter(Admin.account == request.args.get('account')).first()
    print(result.username)
    print(result.password)
    print(result.sex)
    print(result.intro)
    if not result:
        return jsonify({
            'state': 0,
            'data': 'The admin is not existed'
        }), 404
    return jsonify({
        'state': 1,
        'data': {
            "admin_id": result.admin_id,
            'account': result.account,
            "username": result.username,
            "password": result.password,
            "email": result.email,
            "phone": result.phone,
            "sex": result.sex,
            "intro": result.intro,
            "code": result.code,
        }
    }), 200


@admin_blue.route('/projects', methods=['GET'], endpoint='get_admin_projects')
def get_admin_projects():
    try:
        admin = Admin.query.filter(Admin.account == request.args.get('account')).first()
        if not admin:
            return jsonify({
                'state': 0,
                'data': '管理员不存在'
            }), 400
        with open('informationPracticing/static/image.json', 'r', encoding='utf-8') as f:
            image = json.load(f)
        projects = []
        cnt = 1
        for item in admin.projects:
            project = item.to_dict()
            project['image_url'] = image["{}".format(cnt)]
            projects.append(project)
            cnt += 1

        return jsonify({
            'state': 1,
            'data': projects
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'state': 0,
            'data': '发生错误'
        }), 500

