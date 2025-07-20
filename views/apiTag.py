from flask import Blueprint, jsonify, request
from models import Tag
from models import db
from sqlalchemy import or_

tagApi = Blueprint('tagApi', __name__)

@tagApi.route('/tag/create', methods=['POST', 'OPTIONS'])
def createTag():
    if request.method == 'OPTIONS':
        # Trả về phản hồi cho preflight
        return '', 200

    data = request.json
    id = data['id']
    name = data['name']
    color = data['color']
    userId = data['userId']

    tag = Tag.query.filter(Tag.name == name).first()
    if tag:
        return jsonify({
            "message": "Exist Tag, Choose another name"
        })
    else:
        new_tag = Tag(id=id, name=name, color=color, user_id=userId)

        try:
            db.session.add(new_tag)
            db.session.commit()
            res = {
                "data": {
                    "id": new_tag.id,
                    "name": new_tag.name,
                    "color": new_tag.color,
                    "userId": new_tag.user_id
                },
                "success": True,
                "message": "Tag Created"
            }
            return jsonify(res)
        except Exception as e:
            print(f"Error {str(e)}")
            return jsonify({
                "success": False,
                "message": "Error DB"
            })

@tagApi.route('/tag/<string:user_id>', methods=['GET'])
def getTags(user_id):
    tags = Tag.query.filter(or_(Tag.user_id == user_id, Tag.user_id == "0")).all()
    return jsonify([tag.to_dict() for tag in tags])
