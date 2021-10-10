from flask import Blueprint, request, current_app
from app.models.regioes_model import RegioesModel
from app.models.estados_model import EstadosModel

bp_create_estado = Blueprint("bp_create_estado", __name__ )

@bp_create_estado.route("/estado", methods=["POST"])
def create_estado():
    session = current_app.db.session
            
    data = request.get_json()

    # Buscar pela região existente
    regiao = RegioesModel.query.filter_by(nome=data['regiao']).first()
    
    # Retiramos o nome passado pela requisição para colocarmos o id
    # em seu lugar
    data.pop('regiao')

    # Adicionando o id da região para fazer a criação do estado
    data['regiao_id'] = regiao.id
            
    estado = EstadosModel(**data)
            
    session.add(estado)
    session.commit()
            
    return {
        "id": estado.id,
        "nome": estado.nome,
        "sigla": estado.sigla,
        "populacao": estado.populacao,
        "area": float(estado.area),
        "regiao": estado.regiao.nome
    }, 201
    