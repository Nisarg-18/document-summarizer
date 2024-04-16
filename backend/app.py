from flask import Flask
from routes import routes
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
