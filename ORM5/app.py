from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from environs import Env

env = Env()
env.read_env()

db = SQLAlchemy()
mg = Migrate()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bruno:1234@localhost:5432/dealership'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False

    db.init_app(app)
    from models import Car

    mg.init_app(app, db)

    return app