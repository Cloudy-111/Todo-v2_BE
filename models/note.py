from . import db

class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    content = db.Column(db.Text, nullable=False)
    color = db.Column(db.String(255), nullable=True)
    backgroundId = db.Column(db.Integer, nullable=True)
    userId = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Note %r>' % self.id

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'color': self.color,
            'backgroundId': self.backgroundId,
            'userId': self.userId,
        }