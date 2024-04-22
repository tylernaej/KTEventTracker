from .db import db

class Weapon_Critical_Rule(db.Model):
    __tablename__ = 'weapon_rules'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<{self.name} is a weapon critical rule>'