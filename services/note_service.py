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

def getAllNote(data):
    try:
        userId = data['userId']

        notes = Note.query.filter(Note.userId == userId).all()
        return jsonify([note.to_dict() for note in notes])
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "message": str(e),
            "success": False,
        }), 400

def editNote(data):
    try:
        id = data['id']
        header = data['header']
        content = data['content']
        color = data['color']
        userId = data['userId']
        backgroundId = data['backgroundId']

        note = Note.query.filter(Note.id == id).first()
        note.title = header
        note.content = content
        note.color = color
        note.backgroundId = backgroundId

        db.session.add(note)
        db.session.commit()
        return jsonify({
            "success": True,
            "message": "Note Updated"
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "message": str(e),
            "success": False,
        })