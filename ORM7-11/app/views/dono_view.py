from flask import Blueprint, request, current_app, jsonify
from app.models.dono_model import DonoModel

bp = Blueprint("dono", __name__)

@bp.route("/donos", methods=["POST"])
def create():
    data = request.get_json()
    new_owner = DonoModel(
        nome= data["nome"],
        genero= data["genero"],
        idade= data["idade"],
        cachorro_id= data["cachorro_id"]
    )

    session = current_app.db.session

    session.add(new_owner)

    session.commit()

    return jsonify(new_owner)