from datetime import datetime
from models.note import Note
from models import db
from flask import jsonify
import traceback

def createNote(data):
    id = data['id']
    header = data['header']
    content = data['content']
    color = data['color']
    userId = data['userId']
    backgroundId = data['backgroundId']

    newNote = Note(id=id, title=header, content=content, color=color, backgroundId=backgroundId, userId=userId)
    try:
        db.session.add(newNote)
        db.session.commit()
        res = {
            "success": True,
            "message": "Note Created"
        }
        return jsonify(res)
    except Exception as e:
        print(f"Error {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error DB"
        })