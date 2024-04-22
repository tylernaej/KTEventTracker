from .db import db

class Weapon(db.Model):
    __tablename__ = 'weapons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    multi_profiled = (db.Integer)
    profile_1_subname= (db.String(100), nullable=False)
    profile_1_attacks_characteristic= (db.Integer, nullable=False) 
    profile_1_ballistic_skill= (db.Integer, nullable=False) 
    profile_1_normal_damage= (db.Integer, nullable=False) 
    profile_1_critical_damage= (db.Integer, nullable=False) 
    profile_2_subname= (db.String(100)) 
    profile_2_attacks_characteristic= (db.Integer) 
    profile_2_ballistic_skill= (db.Integer) 
    profile_2_normal_damage= (db.Integer) 
    profile_2_critical_damage= (db.Integer) 
    profile_3_subname= (db.String(100)) 
    profile_3_attacks_characteristic= (db.Integer) 
    profile_3_ballistic_skill= (db.Integer) 
    profile_3_normal_damage= (db.Integer) 
    profile_3_critical_damage= (db.Integer) 

    profile_1_special_rules= (db.Integer) 
    profile_1_critical_rules= (db.Integer) 
    profile_2_special_rules= (db.Integer) 
    profile_2_critical_rules= (db.Integer) 
    profile_3_special_rules= (db.Integer) 
    profile_3_critical_rules= (db.Integer) 
