from app import db
from sqlalchemy import Integer, Column, String

class Car(db.Model):
    id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)
    carmaker = Column(String(255), nullable=False)