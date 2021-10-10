from app.configs.database import db

bacias_estados = db.Table('bacias_estados',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('bacia_id', db.Integer, db.ForeignKey('bacias_hidrograficas.id')),
    db.Column('estado_id', db.Integer, db.ForeignKey('estados.id'))
) 