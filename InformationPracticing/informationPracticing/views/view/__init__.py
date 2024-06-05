from flask.blueprints import Blueprint

root_blue = Blueprint('root_blue', __name__, url_prefix='/')
from . import view
