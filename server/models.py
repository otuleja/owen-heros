from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    hero_power = db.relationship("HeroPower" , backref = "heroes" )
    powers = association_proxy("hero_power", "power")

    def __repr__(self):
        return f"<Hero: id = {self.id}, name = {self.name} super_name = {self.super_name}, powers = {self.powers}>"
    
    def to_dict(self):
        return{
            "id" : self.id,
            "name": self.name,
            "super_name": self.super_name,
        }
    
    def show_dict_with_powers(self): 
        my_powers = []
        for power in self.powers:
            my_powers.append(power.to_dict())
        return {
            "id" : self.id,
            "name": self.name,
            "super_name": self.super_name,
            "powers": my_powers
        }

class HeroPower(db.Model):
    __tablename__ = "hero_powers" 

    id = db.Column(db.Integer, primary_key = True)
    strength = db.Column(db.String) 
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("power.id"))

    @validates("strength")
    def validate(self, key , value):
        if value != "Strong" and value != "Weak" and value != "Average":
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
    hero_power = db.relationship("HeroPower" , backref = "power" )
    heroes = association_proxy("hero_power", "heroes")

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
            # "hero_power": self.hero_power,
            # "heroes": self.heroes
        }
# add any models you may need. 