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

@userApi.route('/user/<string:user_id>', methods=['GET'])
def getUser(user_id):
    user = User.query.filter(User.id == user_id).first()
    if user:
        return jsonify({
            "data": {
                "id": user.id,
                "username": user.username,
                "avatar": user.avatar,
                "email": user.email,
            },
            "success": True,
            "message": "Get User Success"
        })
    else:
        return jsonify({
            "success": False,
            "message": "User not found"
        })

@userApi.route('/user/updateAvatar', methods=['POST'])
def updateAvatar():
    data = request.get_json()
    avatar = data.get('avatar')
    userId = data.get('userId')
    if avatar:
        user = User.query.filter(User.id == userId).first()
        user.avatar = avatar
        db.session.commit()
        return jsonify({
            "success": True,
            "message": "Avatar Updated Successfully"
        })
    else:
        return jsonify({
            "success": False,
            "message": "User not found"
        })

@userApi.route('/user/updatePassword', methods=['POST'])
def updatePassword():
    data = request.get_json()
    password = data.get('newPassword')
    userId = data.get('userId')

    user = User.query.filter(User.id == userId).first()
    if user:
        user.password = password
        db.session.commit()
        return jsonify({
            "success": True,
            "message": "Password Updated Successfully"
        })
    else:
        return jsonify({
            "success": False,
            "message": "User not found"
        })

@userApi.route('/user/password/<string:user_id>', methods=['GET'])
def getUserWithPassword(user_id):
    user = User.query.filter(User.id == user_id).first()
    if user:
        return jsonify({
            "data": {
                "id": user.id,
                "username": user.username,
                "avatar": user.avatar,
                "email": user.email,
                "password": user.password,
            },
            "success": True,
            "message": "Get User Success"
        })
    else:
        return jsonify({
            "success": False,
            "message": "User not found"
        })