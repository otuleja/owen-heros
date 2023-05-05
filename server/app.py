#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Hero , Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.get("/heroes")
def get_heroes():
    heroes = Hero.query.all()
    return [hero.to_dict() for hero in heroes]

app.get("/heroes/<int:id>")
def get_heroes(id):
    try:
        hero =Hero.query.get(id)
        return hero.to_dict()
    
    
@app.get("/powers")
def get_power():
    powers = Power.query.all()
    return [power.to_dict() for power in powers]

@app.patch("/powers/<int:id>")
def patch_powers():


@app.post("/hero_powers")
def get_powers():
    





if __name__ == '__main__':
    app.run(port=5555, debug=True)
