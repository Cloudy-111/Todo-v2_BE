from . import db

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Tag {self.name}>'

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'color': self.color, 'user_id': self.user_id}