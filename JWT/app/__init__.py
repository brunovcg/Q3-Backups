from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

app = Flask(__name__)

# TODO: Retirar a chave do código fonte
app.config["JWT_SECRET_KEY"] = "Kenzi3"
jwt = JWTManager(app)


# Rota para receber os dados de login
@app.route("/auth", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # Usar sua função de verificação aqui
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


# Para proteger uma rota use @jwt_required
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # A função get_jwt_identity retorna a identidade do dono 
    # do token quando necessário
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


def create_app():
    return app