from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Instanciando o Flask
app = Flask(__name__)

# Conectando a aplicação ao banco de dados.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bruno:1234@localhost:5432/model_exemple'

# A opção TRACK_MODIFICATIONS é depreciated, ela envia um aviso antes e 
# depois de uma alteração ser confirmada no banco de dados.
# Por isso, iremos desativá-la.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuramos o SQLAlchemy com o flask, agora precisamos instanciar ele.
db = SQLAlchemy(app)

class ProductModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(244))



