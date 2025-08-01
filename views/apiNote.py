from flask import Blueprint, jsonify, request
from models.note import Note
from models import db
from sqlalchemy import or_

from services import note_service

noteApi = Blueprint('noteApi', __name__)

@noteApi.route('/note/create', methods=['POST', 'OPTIONS'])
def createNote():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.json
    return note_service.createNote(data)

@noteApi.route('/note/getAll', methods=['POST', 'OPTIONS'])
def getAllNote():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.json
    return note_service.getAllNote(data)

@noteApi.route('/note/<string:noteId>', methods=['GET', 'OPTIONS'])
def getNote(noteId):
    if request.method == 'OPTIONS':
        return '', 200
    note = Note.query.get(noteId)
    if note:
        return jsonify(note.to_dict())
    else:
        return jsonify({
            "success": False,
            "message": "Note not found",
            "noteId": noteId
        })

@noteApi.route('/note/edit', methods=['POST', 'OPTIONS'])
def editNote():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.json
    return note_service.editNote(data)

@noteApi.route('/note/delete/<string:noteId>', methods=['DELETE', 'OPTIONS'])
def deleteNote(noteId):
    if request.method == 'OPTIONS':
        return '', 200

    note = Note.query.get(noteId)
    if note:
        db.session.delete(note)
        db.session.commit()
        return jsonify({
            "success": True,
            "message": "Note deleted",
        })
    else:
        return jsonify({
            "success": False,
            "message": "Note not found",
        })