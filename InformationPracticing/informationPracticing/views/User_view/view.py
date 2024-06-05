from informationPracticing.models import *
from ..User_view import user_blue
from flask_login import login_required
from flask import jsonify, request
from exert import db

import json


@user_blue.route('/', methods=['GET'], endpoint='get_users')
def get_users():
    try:
        project = Project.query.filter(Project.title == request.args.get('title')).first()
        users = []
        cnt = 19
        with open('informationPracticing/static/image_u.json', 'r', encoding='utf-8') as f:
            image = json.load(f)

        for items in project.users:
            user = items.to_dict()
            user['image_url'] = image[f"{cnt}"]
            users.append(user)
            cnt += 1
        print(users)
        return jsonify({
            'state': 1,
            'data': users
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'state': 0,
            'data': '志愿者查询失败'
        }), 400


@user_blue.route('/', methods=['POST'], endpoint='add_user')
def add_user():
    try:
        name = request.form.get('name')
        phone = request.form.get('phone')

        user = User(name=name, phone=phone)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'state': 1,
            'data': '志愿者添加成功'
        }), 200
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({
            'state': 0,
            'data': '志愿者添加失败'
        }), 400


# @user_blue.route('/update', methods=['POST'], endpoint='')
@user_blue.route('/rank', methods=['GET'], endpoint='get_users_rank')
def rank():
    try:
        user_rank = []
        users = User.query.all()

        for user in users:
            projects = user.projects
            volunteer_time = 0
            for project in projects:
                if project.is_start:
                    volunteer_time += project.value
            user_rank.append({
                'name': user.name,
                'time': volunteer_time
            })

        sorted_user = sorted(user_rank, key=lambda key: key['time'], reverse=True)
        user_rank: [dict] = []
        rank, min_time = 0, 0x3f3f3f3f
        for item in sorted_user:
            time = item.get('time')
            if time < min_time:
                min_time = time
                rank += 1
            user_rank.append({
                'rank': rank,
                'name': item.get('name'),
                'time': time
            })
        print(user_rank)
        return jsonify({
            'state': 1,
            'data': user_rank
        }), 200
    except Exception as e:
        print(e)
        jsonify({
            'state': 0,
            'data': '排名表查询错误'
        }), 400


@user_blue.route('/activate', methods=["POST"], endpoint='update_user_activate')
def update_user_activate():
    try:
        name = request.args.get('name')
        user = User.query.filter(User.name == name).first()
        user.judge = True

        db.session.commit()
        return jsonify({
            'state': 1,
            'data': '用户审核成功'
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'state': 0,
            'data': '用户审核失败'
        }), 400
