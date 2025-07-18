from flask import Blueprint, jsonify, request
from models import User
from models import db

userApi = Blueprint('userApi', __name__)

@userApi.route('/user/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    try:
        user = User.query.filter(User.username == username, User.password == password).first()
        print(user)
        if user:
            res = {
                "user_id": user.id,
                "success": True,
                "message": "Login Success"
            }
            return jsonify(res)
        else:
            return jsonify({
                "success": False,
                "message": "Username , password wrong"
            })
    except Exception as e:
        print(f"Error {str(e)}")
        return jsonify({
            "success": False,
            "message": "Failed to Login"
        })

@userApi.route('/user/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    avatar = data.get('avatar')
    id = data.get('id')

    user = User.query.filter(User.username == username).first()
    if user:
        return jsonify({
            "message": "Exist Username, Choose another username"
        })
    else:
        new_user = User(id=id, username=username, password=password, avatar=avatar, email=email)

        try:
            db.session.add(new_user)
            user = User.query.filter(User.username == username).first()
            db.session.commit()
            res = {
                "user_id": user.id,
                "success": True,
                "message": "Register Successfully"
            }
            return jsonify(res)
        except Exception as e:
            print(f"Error {str(e)}")
            return jsonify({
                "success": False,
                "message": "Error DB"
            })

@userApi.route("/users", methods=['GET'])
def getUsers():
    users = User.query.all()
    return jsonify([(c.username, c.id, c.email, c.password, c.avatar) for c in users])