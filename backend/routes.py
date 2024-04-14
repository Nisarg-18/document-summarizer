from flask import jsonify, Blueprint
from controllers import get_home

routes = Blueprint('routes', __name__, static_folder='static',
                   template_folder='templates')


@routes.route('/', methods=['GET'])
def home():
    return jsonify(get_home()), 200
