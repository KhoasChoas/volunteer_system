from flask import Blueprint

user_blue = Blueprint('User', __name__, url_prefix='/user')
from . import view
