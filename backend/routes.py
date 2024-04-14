from flask import jsonify, Blueprint, request
from controllers import get_home, upload
from werkzeug.utils import secure_filename
import os

routes = Blueprint('routes', __name__, static_folder='static',
                   template_folder='templates')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}


@routes.route('/', methods=['GET'])
def home():
    return jsonify(get_home()), 200


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
            "error": "File not added"
        }
        return jsonify(response), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        max_length = int(request.form.get('max_length'))
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        summary = upload(filename=UPLOAD_FOLDER+'/' +
                         filename, max_length=max_length)
        response = {
            "success": True,
            "summary": summary
        }
        os.remove(UPLOAD_FOLDER+'/'+filename)
        return jsonify(response)
    else:
        response = {
            "success": False,
            "error": "File is not of type PDF"
        }
        return jsonify(response), 400
