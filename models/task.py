from . import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    note = db.Column(db.Text)

    start_time = db.Column(db.Integer)
    end_time = db.Column(db.Integer)
    remind_at = db.Column(db.Integer)
    create_at = db.Column(db.Integer)

    is_completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.Integer)

    priority_id = db.Column(db.String(36), db.ForeignKey('priorities.id'), nullable=True)
    tag_id = db.Column(db.String(36), db.ForeignKey('tags.id'), nullable=True)
    is_progress_task = db.Column(db.Boolean, default=False)
    success_rate = db.Column(db.Float)

    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'note': self.note,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'remind_at': self.remind_at,
            'create_at': self.create_at,
            'is_completed': self.is_completed,
            'completed_at': self.completed_at,
            'priority_id': self.priority_id,
            'tag_id': self.tag_id,
            'is_progress_task': self.is_progress_task,
            'success_rate': self.success_rate,
            'user_id': self.user_id
        }