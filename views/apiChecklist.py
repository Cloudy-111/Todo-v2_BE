import traceback

from flask import Blueprint, jsonify, request
from sqlalchemy.event import api
from models import db
from sqlalchemy import or_

from models.checklist import Checklist

checklistApi = Blueprint('checklistApi', __name__)

@checklistApi.route('/checklist/create', methods=['POST', 'OPTIONS'])
def createChecklist():
    data = request.get_json()
    try:
        checkList = Checklist(**data)
        db.session.add(checkList)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "checklist created successfully",
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "success": False,
            "message": str(e),
        })

@checklistApi.route('/checklist/getAllByTaskId/<string:taskId>', methods=['GET', 'OPTIONS'])
def getAllChecklistByTaskId(taskId):
    checklistItems = Checklist.query.filter_by(taskId=taskId).all()
    return jsonify([checklist.to_dict() for checklist in checklistItems])

@checklistApi.route('/checklist/toggleCompleted', methods=['PUT', 'OPTIONS'])
def toggleChecklistCompleted():
    try:
        item_ids = request.json
        for item_id in item_ids:
            item = Checklist.query.get(item_id)
            if item:
                item.isCompleted = not item.isCompleted
        db.session.commit()
        return jsonify({
            "success": True,
            "message": "checklist completed successfully",
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "success": False,
            "message": str(e),
        })