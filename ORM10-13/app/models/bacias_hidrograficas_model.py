from app.configs.database import db
from app.models.bacias_estados_table import bacias_estados

class BaciasHidrograficasModel(db.Model):
    __tablename__ = "bacias_hidrograficas"
            
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    area = db.Column(db.Integer)
            
    estados = db.relationship("EstadosModel", secondary=bacias_estados, backref="bacias")