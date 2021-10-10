from flask import Flask
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')


# Simulando lista de tokens cadastrados em um DB
tokens = {
    "58fddba0-ed80-42da-b276-7b3144c2374d": "john",
    "ea1832e0-2548-400d-97a1-b8cc88fb0475": "susan"
}

#Função que verifica no DB se o token existe e retorna o usuário
@auth.verify_token
def verify_token(token):
    if token in tokens:
        # Retorna o usuário atrelado ao token
        return tokens[token]


# Rota protegida pelo API token
@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())

def create_app():
    return app