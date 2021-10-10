from flask import Blueprint, request, current_app
from app.models.bacias_hidrograficas_model import BaciasHidrograficasModel as BHM

bp_create_bacia_hidrografica = Blueprint("bp_create_bacia_hidrografica", __name__)

@bp_create_bacia_hidrografica.route("/bacia_hidrografica", methods=["POST"])
def create_bacia_hidrografica():
    session = current_app.db.session
          
    data = request.get_json()
          
    bacia_hidrografica = BHM(**data)
          
    session.add(bacia_hidrografica)
    session.commit()
          
    return {
        "id": bacia_hidrografica.id,
        "nome": bacia_hidrografica.nome,
        "area": bacia_hidrografica.area,
    }, 201