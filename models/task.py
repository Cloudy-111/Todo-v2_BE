from . import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    note = db.Column(db.Text)

    startTime = db.Column(db.BigInteger)
    endTime = db.Column(db.BigInteger)
    remindAt = db.Column(db.BigInteger)
    createAt = db.Column(db.BigInteger)

    isCompleted = db.Column(db.Boolean, default=False)
    completedAt = db.Column(db.Integer)

    priorityId = db.Column(db.String(36), db.ForeignKey('priorities.id'), nullable=True)
    tagId = db.Column(db.String(36), db.ForeignKey('tags.id'), nullable=True)
    isProgressTask = db.Column(db.Boolean, default=False)
    successRate = db.Column(db.Float)

    userId = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'note': self.note,
            'startTime': self.startTime,
            'endTime': self.endTime,
            'remindAt': self.remindAt,
            'createAt': self.createAt,
            'isCompleted': self.isCompleted,
            'completedAt': self.completedAt,
            'priorityId': self.priorityId,
            'tagId': self.tagId,
            'isProgressTask': self.isProgressTask,
            'successRate': self.successRate,
            'userId': self.userId
        }