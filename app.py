from flask import Flask, jsonify
from views import apiUser, apiTag, apiPriority
from models import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_v2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask"}), 200
app.register_blueprint(apiUser.userApi)

db.init_app(app)
app.register_blueprint(apiTag.tagApi)

app.register_blueprint(apiPriority.priorityApi)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    print(app.url_map)

    app.run(host="0.0.0.0",debug=True, port=5000)
