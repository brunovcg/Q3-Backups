from flask import Flask

from .cachorro_view import bp as bp_cachorro
from .dono_view import bp as bp_dono

def init_app(app: Flask):
    app.register_blueprint(bp_cachorro)
    app.register_blueprint(bp_dono)