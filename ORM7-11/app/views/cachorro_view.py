from flask import Blueprint, request, current_app, jsonify
from app.models.cachorro_model import CachorroModel

bp = Blueprint("cachorro", __name__)

@bp.route("/cachorros", methods=["POST"])
def create():
    data = request.get_json()
    new_dog = CachorroModel(
        nome=data["nome"],
        raca=data["raca"],
        idade=data["idade"]
    )

    session = current_app.db.session

    session.add(new_dog)
    session.commit()

    return jsonify(new_dog)