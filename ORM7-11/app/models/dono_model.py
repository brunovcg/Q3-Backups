from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

from app.models.cachorro_model import CachorroModel

@dataclass
class DonoModel(db.Model):
    id: int
    nome: str
    genero: str
    cachorro: CachorroModel

    __tablename__ = "donos"
    
    id = Column(Integer, primary_key=True)
    
    nome = Column(String, nullable=False)
    idade = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    
    cachorro_id = Column(
        Integer, ForeignKey("cachorros.id"), nullable=False, unique=True
    )
    
    cachorro = relationship("CachorroModel", backref=backref("dono", uselist=False))