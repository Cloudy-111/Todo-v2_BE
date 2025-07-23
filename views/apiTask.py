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

@taskApi.route('/task/delete/<string:taskId>', methods=['DELETE'])
def deleteTask(taskId):
    task = Task.query.get(taskId)
    if task:
        try:
            db.session.delete(task)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Task deleted'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': str(e)})
    return jsonify({'success': False, 'message': 'Task not found'})

@taskApi.route('/task/<string:taskId>', methods=['GET'])
def getTask(taskId):
    task = Task.query.get(taskId)
    if task:
        return jsonify(task.to_dict())
    return jsonify({'success': False, 'message': 'Task not found'})

@taskApi.route('/task/completed/<string:taskId>', methods=['PUT', 'OPTIONS'])
def completeTask(taskId):
    return task_service.complete_task(taskId)

@taskApi.route('/task/updateProgress/<string:taskId>', methods=['POST', 'OPTIONS'])
def updateProgress(taskId):
    task = Task.query.get(taskId)
    data = request.json
    if task:
        task.successRate = data['successRate']
        db.session.commit()
        return jsonify({
            "success": True,
            "message": "Task updated successfully",
            "taskId": task.id
        })
    else:
        return jsonify({
            "success": False,
            "message": "Task not found",
        })