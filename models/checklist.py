from . import db

class Checklist(db.Model):
    __tablename__ = 'checklist'

    id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    isCompleted = db.Column(db.Boolean, nullable=False)
    taskId = db.Column(db.String(36), db.ForeignKey('tasks.id'), nullable=False)

    def __repr__(self):
        return f'<Checklist {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'isCompleted': self.isCompleted,
            'taskId': self.taskId
        }