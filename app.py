from flask import Flask, jsonify
from views import apiUser
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_v2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask"}), 200
app.register_blueprint(apiUser.userApi)

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()

    print(app.url_map)

    app.run(host="0.0.0.0",debug=True, port=5000)
