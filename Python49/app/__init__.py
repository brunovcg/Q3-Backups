from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bruno:1234@localhost:5432/python49'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # E-mails devem ser únicos
    email = db.Column(db.String(80), nullable=False, unique=True)

    # COLUNA DA SENHA CRIPTOGRAFADA
    # PASSWORD_HASH não é obrigátorio na hora da requisição, o usuário
    # vai nos informar a senha e em seguida utilizamos um
    # algoritimo de hash para atribuir valor no PASSWORD_HASH
    password_hash = db.Column(db.String, nullable=True)


    # Resumidamente, o @property é uma maneira pythonica 
    # de se utilizar getter e setter
    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    # Recebe a senha do usuário, em seguida faz o HASH 
    # e atribui a coluna PASSWORD_HASH
    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    # Recebe a senha do usuário, em seguida faz o hash e compara 
    # se é igual a armazenada no bando de dados
    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)


@app.route("/users", methods=["POST"])
def create_user():
    # Pegando os dados da requisição
    user_data = request.get_json()

    # Removendo a propriedade PASSWORD dos dados da requisição e
    # atribuindo esse valor na variável password_to_hash
    password_to_hash = user_data.pop("password")
    
    # Criando um novo usuário, perceba que estamos criando o usuário
    # sem o password, pois removemos pra fazer o hash da senha
    new_user = Users(**user_data)

    # Com o novo usuário criado, chamamos o SETTER PASSWORD, pra fazer o hash
    # da senha e atribuir a senha "hasheada" na coluna PASSWORD_HASH
    new_user.password = password_to_hash

    # E pra finalizar salvar essas alterações no banco
    db.session.add(new_user)
    db.session.commit()

    return {"message": "User created"}, 200


    # rodar db.create_all() no prompt 1 vez


@app.route("/login", methods=["POST"])
def login():
    # Pegando os dados da requisição
    user_data = request.get_json()

    # Encontrando o usuário no banco de dados, como o e-mail é único, 
    # utilizamos ele de filtro para encontrar o usuário
    found_user: Users = Users.query.filter_by(email=user_data["email"]).first()

    # Se não encontrarmos o usuário, encerramos a requisição
    if not found_user:
        return {"message": "User not found"}, 404

    # Se encontrarmos o usuário, precisamos utilizar o método VERIFY_PASSWORD, 
    # que irá fazer o hash da senha enviada e comparar com a do usuário
    # cadastrada no banco de dados. Se a senha for correta retornamos 
    # que o login foi um sucesso. Caso a senha esteja incorreta, 
    # informamos que o usuário não está autorizado a fazer o login
    if found_user.verify_password(user_data["password"]):
        return {"message": "Sucess login"}, 200
    else:
        return {"message": "Unauthorized"}, 401