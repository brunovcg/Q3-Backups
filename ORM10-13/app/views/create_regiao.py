from flask import Blueprint, request, current_app
from app.models.regioes_model import RegioesModel

bp_create_regiao = Blueprint("bp_create_regiao", __name__)

@bp_create_regiao.route("/regiao", methods=["POST"])
def create_regiao():
    session = current_app.db.session

    data = request.get_json()

    regiao = RegioesModel(**data)

    session.add(regiao)
    session.commit()

    return {
        "id": regiao.id,
        "nome": regiao.nome,
        "numero estados": regiao.numero_estados,
    }