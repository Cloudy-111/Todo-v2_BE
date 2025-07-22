from flask import Blueprint, jsonify, request
from models import Priority
from models import db
from sqlalchemy import or_

priorityApi = Blueprint('priority_api', __name__)

@priorityApi.route('/priority', methods=['GET'])
def get_priority():
    priorities = Priority.query.all()
    return jsonify([priority.to_dict() for priority in priorities])

@priorityApi.route('/priority/<string:priority_id>', methods=['GET'])
def get_priority_by_id(priority_id):
    priority = Priority.query.get(priority_id)
    return jsonify(priority.to_dict())