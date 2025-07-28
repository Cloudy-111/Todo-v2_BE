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
    day_millis = convert_date_string_to_millis(daySelect)
    start_of_day = day_millis
    end_of_day = day_millis + 86400000  # +1 ngày (ms)

    return startTime < end_of_day and endTime >= start_of_day

def convert_date_string_to_millis(dateString):
    try:
        date = datetime.strptime(dateString, '%Y/%m/%d')
        millis = date.timestamp() * 1000
        return millis
    except Exception as e:
        traceback.print_exc()
        return -1

def datetime_to_millis(date):
    return int(date.timestamp() * 1000)

def complete_task(taskId):
    task = Task.query.get(taskId)
    if task:
        task.isCompleted = True
        task.completedAt = datetime_to_millis(datetime.utcnow())
        task.successRate = 1
        db.session.commit()
        return jsonify({
            "success": True,
            "message": "Task completed",
            "taskId": taskId,
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Task not found",
        }), 404

def getTasksLimited(data):
    try:
        amount = int(data['amount'])
        userId = data['userId']
        tagIds = data.get('tagIds', [])

        tasks = fetch_tasks_by_tags_limited(userId, tagIds, amount)
        return jsonify([task.to_dict() for task in tasks])
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "message": str(e),
            "success": False,
        }), 400

def fetch_tasks_by_tags_limited(userId, tagIds, amount):
    result = []
    for tag_id in tagIds:
        q = (Task.query
             .filter(Task.userId == userId, Task.tagId == tag_id)
             .order_by(Task.startTime.asc())
             .limit(amount)
             .all())
        result.extend(q)
    return result

def getTasksByTagId(data):
    try:
        userId = data['userId']
        tagId = data['tagId']

        tasks = (Task.query
                 .filter(Task.userId == userId, Task.tagId == tagId)
                 .order_by(Task.startTime.asc())
                 .all())
        return jsonify([task.to_dict() for task in tasks])
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "message": str(e),
            "success": False,
        }), 400

def searchTask(data):
    try:
        userId = data['userId']
        query = data['query']

        tasks = Task.query.filter(Task.userId == userId, Task.title.ilike(f"%{query}%")).limit(5).all()
        return jsonify([task.to_dict() for task in tasks])
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "message": str(e),
            "success": False,
        }), 400