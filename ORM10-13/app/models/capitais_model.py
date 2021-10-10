from app.configs.database import db

class CapitaisModel(db.Model):    
    __tablename__ = 'capitais'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    bairros = db.Column(db.Integer)
    populacao = db.Column(db.Integer)
    estado = db.relationship("EstadosModel", backref=db.backref("capital", uselist=False))
    estado_id = db.Column(db.Integer, db.ForeignKey("estados.id"), nullable=False, unique=True)
    