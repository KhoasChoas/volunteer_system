from flask import Blueprint

project_blue = Blueprint('project', __name__, url_prefix='/project')
from . import view
