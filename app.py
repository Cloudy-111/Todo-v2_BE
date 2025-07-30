from flask import Flask, jsonify
from views import apiUser, apiTag, apiPriority, apiTask, apiChecklist, apiNote
from models import db
from models.note import Note
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

app.register_blueprint(apiChecklist.checklistApi)

app.register_blueprint(apiTask.taskApi)

app.register_blueprint(apiPriority.priorityApi)

app.register_blueprint(apiNote.noteApi)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    print(app.url_map)

    app.run(host="0.0.0.0",debug=True, port=5000)
