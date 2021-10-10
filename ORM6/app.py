from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from environs import Env

def create_app() -> Flask:
    app = Flask(__name__)
    env = Env()
    env.read_env()

    app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

    class SalgadoModel(db.Model):
        __tablename__ = 'salgados'

        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String(60), nullable=False, unique=True)
        preco = db.Column(db.Float, nullable=False)

    # @dataclass
    # class SalgadoModel(db.Model):
    #     id: int
    #     nome: str
    #     preco: float

    #     __tablename__ = 'salgados'

    #     id = db.Column(db.Integer, primary_key=True)
    #     nome = db.Column(db.String(60), nullable=False, unique=True)
    #     preco = db.Column(db.Float, nullable=False)
   
    #     return jsonify(salgado)
    # return app
        
    db.create_all()

    @app.route('/api/salgados', methods=['POST'])
    def criar_salgado():
        data = request.get_json()

        salgado = SalgadoModel(**data)

        db.session.add(salgado)
        db.session.commit()

        return {'id': salgado.id, 'nome': salgado.nome, 'preco': salgado.preco}

    return app
