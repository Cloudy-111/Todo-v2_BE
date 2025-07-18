from . import db

class Priority(db.Model):
    __tablename__ = 'priorities'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(255), nullable=False)
    level = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Priority {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
            'level': self.level,
        }