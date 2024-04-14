from flask import jsonify, Blueprint, request
from controllers import get_home, upload
from werkzeug.utils import secure_filename
import os

routes = Blueprint('routes', __name__, static_folder='static',
                   template_folder='templates')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


@routes.route('/', methods=['GET'])
def home():
    return jsonify(get_home()), 200


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@routes.route('/upload-document', methods=['POST'])
def upload_doc():
    if 'file' not in request.files:
        response = {
            "success": False,
            "error": "File not added"
        }
        return jsonify(response), 400
    file = request.files['file']
    if file.filename == '':
        response = {
            "success": False,
            "error": "File invalid"
        }
        return jsonify(response), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return jsonify(upload(filename=UPLOAD_FOLDER+'/'+filename))
