from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, ValidationError

from informationPracticing.models import Code, Admin


class RegistrationForm(FlaskForm):
    username = StringField(label='用户名',
                           validators=[DataRequired(message='用户名必须填写'),
                                       Length(min=1, max=12, message='用户名长度必须在1到12位之间'),
                                       Regexp(r'^[\u4e00-\u9fa5a-zA-Z0-9]+$', message='用户名不允许包含特殊字符'),
                                       ]
                           )
    account = StringField(label='账号',
                          validators=[DataRequired(message='账号必须填写'),
                                      Length(min=10, max=20, message='账号长度必须在10到20位之间'),
                                      Regexp(r'^\d+$', message='账号仅包含数字'),
                                      ]
                          )
    password = PasswordField(label='密码',
                             validators=[DataRequired(message='密码必须填写'),
                                         Length(min=10, max=20, message='密码长度必须在10到20位之间'),
                                         Regexp(r'^(?=.*\d)(?=.*[a-zA-Z])(?=.*[^\da-zA-Z\s]).{10,20}$',
                                                message='密码必须包含数字、字符、特殊字符'),
                                         ]
                             )
    confirm_password = PasswordField(label='确认密码',
                                     validators=[DataRequired('确认密码必须填写'),
                                                 EqualTo('password', '两次密码不一致'),
                                                 ]
                                     )
    code = StringField(label='邀请码',
                       validators=[DataRequired('邀请码必须填写')])

    def __repr__(self):
        return f'用户名：{self.username}, 账号：{self.account}, 密码：{self.password}'

    def validate_code(self, field):
        if not Code.query.get(field.data):
            raise ValidationError('邀请码错误')

    def validate_username(self, field):
        if Admin.query.filter(Admin.username == field.data).first():
            raise ValidationError('用户已存在')


class LoginForm(FlaskForm):
    account = StringField(label='账号',
                          validators=[DataRequired(message='账号必须填写'),
                                      Length(min=10, max=20, message='账号长度必须在10到20位之间'),
                                      Regexp(r'^\d+$', message='账号仅包含数字'),
                                      ]
                          )
    password = PasswordField(label='密码',
                             validators=[DataRequired(message='密码必须填写'),
                                         Length(min=10, max=20, message='密码长度必须在10到20位之间'),
                                         Regexp(r'^(?=.*\d)(?=.*[a-zA-Z])(?=.*[^\da-zA-Z\s]).{10,20}$',
                                                message='密码必须包含数字、字符、特殊字符'),
                                         ]
                             )

    def validate_account(self, field):
        if not Admin.query.filter(Admin.account == field.data).first():
            print("No")
            raise ValidationError('账号错误')


class ProjectForm(FlaskForm):
    title = StringField(label='标题',
                        validators=[DataRequired(message='志愿活动标题必须填写'),
                                    Length(min=2, max=30, message='标题长度必须在2到30位之间'),
                                    ]
                        )
    start_time = StringField(label='开始时间',
                             validators=[DataRequired(message='开始时间必须填写'),
                                         Regexp(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$', message='时间格式不正确')
                                         ]
                             )
    end_time = StringField(label='结束时间',
                           validators=[DataRequired(message='结束时间必须填写'),
                                       Regexp(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$', message='时间格式不正确')
                                       ]
                           )
    situation_province = StringField(label='省份',
                                     validators=[DataRequired('志愿活动省份必须填写')])
    situation_city = StringField(label='省份',
                                 validators=[DataRequired('志愿活动省市必须填写')])
    require_num = IntegerField(label='志愿活动所需人数',
                               validators=[DataRequired(message='活动所需人数必须填写')])
    value = IntegerField(label='志愿活动提供的志愿时长',
                         validators=[DataRequired(message='志愿活动提供的志愿时长必须填写')])

    def __repr__(self):
        return f'名称：{self.title}, 开始时间: {self.start_time}, 结束时间: {self.end_time}'
