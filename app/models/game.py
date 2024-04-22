from .db import db

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.integer, primary_key=True)
    title = db.Column(db.string(100), nullable=False)

    def __repr__(self):
        return f'<{self.title}: is a game>'
        
    def to_dict(self):
        return {
            "id" : self.id,
            "title" : self.title
        }