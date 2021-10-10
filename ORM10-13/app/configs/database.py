from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)        
    app.db = db

    from app.models.estados_model import EstadosModel
    from app.models.capitais_model import CapitaisModel
    
    from app.models.regioes_model import RegioesModel

      # Adicione as novas models que vamos criar
    from app.models.bacias_hidrograficas_model import BaciasHidrograficasModel
    from app.models.bacias_estados_table import bacias_estados