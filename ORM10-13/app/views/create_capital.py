from flask import Blueprint, request, current_app, jsonify
from app.models.capitais_model import CapitaisModel
from app.models.estados_model import EstadosModel
            
bp_create_capital = Blueprint("bp_create_capital", __name__ )

            
@bp_create_capital.route("/capital", methods=["POST"])
def create_capital():
    session = current_app.db.session
            
    data = request.get_json()
    estado = EstadosModel.query.filter_by(nome=data["estado_nome"]).first()

    data.pop("estado_nome")
    data["estado_id"] = estado.id
            
    capital = CapitaisModel(**data)
            
    session.add(capital)
    session.commit()
            
    return {
        "id": capital.id,
        "nome": capital.nome,
        "bairros": capital.bairros,
        "populacao": capital.populacao,
        "estado_nome": capital.estado.nome,
    }, 201

    