from ..Project_view import project_blue
from informationPracticing.models import *
from flask_login import current_user, login_required
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from exert import db
from informationPracticing.forms import ProjectForm


@project_blue.route('/', methods=['POST'], endpoint='add_project')
def add_project():
    project_new = ProjectForm()
    # print(project_new)
    if not project_new.validate_on_submit():
        for filed_name, data in project_new.errors.items():
            # print(project_new.errors.get(filed_name)[0])
            return jsonify({
                'state': 0,
                'data': project_new.errors.get(filed_name)[0]
            }), 400
    try:
        title = project_new.title.data
        start_time = project_new.start_time.data
        end_time = project_new.end_time.data
        situation_province = project_new.situation_province.data
        situation_city = project_new.situation_city.data
        require_num = project_new.require_num.data
        value = project_new.value.data
        admin_id = 1

        project = Project(title=title, start_time=start_time, end_time=end_time,
                          situation_province=situation_province, situation_city=situation_city,
                          require_num=require_num, value=value, admin_id=admin_id)
        db.session.add(project)
        db.session.commit()

        return jsonify({
            'state': 0,
            'data': '活动创建成功'
        }), 201

    except IntegrityError as e:
        print(e)
        db.session.rollback()
        return jsonify({
            'state': 0,
            'data': '活动创建错误'
        }), 400
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return jsonify({
            'state': 0,
            'data': '服务器错误'
        }), 500


@project_blue.route('/delete', methods=['POST'], endpoint='delete_project')
def delete_project():
    try:
        title = request.args.get('title')
        project = Project.query.filter(Project.title == title).first()
        db.session.delete(project)
        db.session.commit()
        return jsonify({
            'state': 1,
            'data': '活动删除成功'
        }), 200
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({
            'state': 0,
            'data': '删除失败'
        }), 400


@project_blue.route('/activate', methods=["POST"], endpoint='update_project_activate')
def update_project_activate():
    try:
        title = request.args.get('title')
        project = Project.query.filter(Project.title == title).first()
        project.is_start = True

        db.session.commit()
        return jsonify({
            'state': 1,
            'data': '发布成功'
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'state': 0,
            'data': '发布失败'
        }), 400


@project_blue.route('/update', methods=["POST"], endpoint='update_project')
def update_project():
    project_new = ProjectForm()
    print(project_new)
    if not project_new.validate_on_submit():
        for filed_name, data in project_new.errors.items():
            print(project_new.errors.get(filed_name)[0])
            return jsonify({
                'state': 0,
                'data': project_new.errors.get(filed_name)[0]
            }), 400
    try:
        title = project_new.title.data
        project = Project.query.filter(Project.title == title).first()
        project.start_time = project_new.start_time.data
        project.end_time = project_new.end_time.data
        project.situation_province = project_new.situation_province.data
        project.situation_city = project_new.situation_city.data
        project.require_num = project_new.require_num.data
        project.value = project_new.value.data
        project.admin_id = 1

        db.session.commit()

        return jsonify({
            'state': 1,
            'data': '活动修改成功'
        }), 201

    except IntegrityError as e:
        print(e)
        db.session.rollback()
        return jsonify({
            'state': 0,
            'data': '活动修改错误'
        }), 400
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return jsonify({
            'state': 0,
            'data': '服务器错误'
        }), 500
