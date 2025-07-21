from flask import Blueprint, jsonify, request
from models import Task
from models import db
import traceback

from services import task_service

taskApi = Blueprint('taskApi', __name__)
@taskApi.route('/task/create', methods=['POST', 'OPTIONS'])
def createTask():
    data = request.json
    try:
        task = Task(**data)
        db.session.add(task)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Task created successfully",
            "taskId": task.id
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "message": str(e),
            "success": False,
        }), 400

@taskApi.route('/task/getDayTask', methods=['POST'])
def getDayTask():
    data = request.json
    return task_service.getDayTasks(data)

