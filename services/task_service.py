from datetime import datetime
from models import Task
from models import db
from flask import jsonify
import traceback

def getDayTasks(data):
    try:
        daySelect = data['daySelect']
        userId = data['userId']

        tasks = Task.query.filter(Task.userId == userId).all()
        dayTasks = [task.to_dict() for task in tasks if checkDay(task.startTime, task.endTime, daySelect)]
        return jsonify([task for task in dayTasks])
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "message": str(e),
            "success": False,
        }), 400

def checkDay(startTime, endTime, daySelect):
    if convert_date_string_to_millis(daySelect) >= startTime or convert_date_string_to_millis(daySelect) <= endTime: return True
    return False

def convert_date_string_to_millis(dateString):
    try:
        date = datetime.strptime(dateString, '%Y/%m/%d')
        millis = date.timestamp() * 1000
        return millis
    except Exception as e:
        traceback.print_exc()
        return -1