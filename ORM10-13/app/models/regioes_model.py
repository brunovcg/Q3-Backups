from app.configs.database import db

class RegioesModel(db.Model):
    __tablename__ = 'regioes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    numero_estados = db.Column(db.Integer)
    
    estados = db.relationship("EstadosModel", backref="regiao")