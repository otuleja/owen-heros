from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    heropower = db.relationship("HeroPower" , backref = "heroes" )
    powers = association_proxy("heropowers", "power")

    def __repr__(self):
        return f"<Hero: id = {self.id}, name = {self.name} super_name = {self.super_name}, heropower = {self.heropower} powers = {self.powers}>"
    
    def to_dict(self):
        return{
            "id" : self.id,
            "name": self.name,
            "super_name": self.super_name,
            "heropower": self.heropower,
            "powers": self.powers
        }

class HeroPower(db.Model):
    __tablename__ = "hero_powers" 

    id = db.Column(db.Integer, primary_key = True)
    strength = db.Column(db.String) 
    hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("power.id"))

    @validates("strength")
    def validate(self, key , value):
        if value != "Strong" or value != "weak" or value != "Average":
            raise ValueError ("strength must be on of the following Values Strong, Weak, or Average")
        return value
    
    def __repr__(self):
        return f"<HeroPowers: id = {self.id}, strength = {self.strength}, hero_id ={self.hero_id}, power_id = {self.power_id}>"

    def to_dict(self):
        return{
            "id": self.id,
            "strength": self.strength,
            "hero_id": self.hero_id,
            "power_id": self.power_id
        }



class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String)    
    description = db.Column(db.String)
    heropower = db.relationship("HeroPowers" , backref = "power" )
    heroes = association_proxy("heropowers", "hero")

    @validates("strength")
    def validate(self, key , value):
        if value  < 20:
            raise ValueError("description must be present and at least 20 characters long")
        return value
    
    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "heropower": self.heropower,
            "heroes": self.heroes
        }
# add any models you may need. 