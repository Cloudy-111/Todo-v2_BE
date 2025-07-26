from datetime import datetime
from models import Tag
from models import db
from flask import jsonify
import traceback

def editTag(data):
    try:
        tagId = data['id']
        tagName = data['name']
        tagColor = data['color']

        tag = Tag.query.get(tagId)
        tag.name = tagName
        tag.color = tagColor
        db.session.commit()
        return jsonify({
            "data": {
                "id": tag.id,
                "name": tag.name,
                "color": tag.color,
                "userId": tag.user_id
            },
            "success": True,
            "message": "Tag successfully updated",
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "success": False,
            "message": str(e),
        })