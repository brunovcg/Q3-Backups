from flask import Blueprint, request, current_app
from app.models.bacias_hidrograficas_model import BaciasHidrograficasModel as BHM
from app.models.estados_model import EstadosModel
          
bp_create_bacia_estado = Blueprint("bp_create_bacia_estado", __name__)
          
@bp_create_bacia_estado.route("/bacia_estado", methods=["POST"])
def create_bacia_hidrografica():
    session = current_app.db.session
          
    data = request.get_json()
          
    bacia: BHM = BHM.query.filter_by(nome=data["bacia_nome"]).first()
    estado: EstadosModel = EstadosModel.query.filter_by(nome=data["estado_nome"]).first()

    bacia.estados.append(estado)
    
    session.commit()
          
    return {
      "estado_nome": estado.nome,
      "bacia_nome": bacia.nome,
    }, 201
    