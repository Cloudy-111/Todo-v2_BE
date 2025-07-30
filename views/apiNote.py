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

