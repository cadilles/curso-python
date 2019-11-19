from flask import Flask, Blueprint, request, Response
from config import mongo_db
from bson.json_util import dumps

grupos_routes = Blueprint(
    "grupos",
    __name__,
    url_prefix="/grupos"
)

@grupos_routes.route("", methods=["PATCH"])
def updateGrupo():
    try:
        grupo = request.get_json()
        updated = mongo_db.grupo.update_one(
            { "name": grupo['name'] },
            { "$set": grupo }
        )
        if updated.modified_count:
            response = {"message": "Grupo '%s'  atualizado com sucesso! "%(grupo["name"]) }
            return Response(dumps(response), status=200, content_type="application/json")
        elif updated.matched_count:
            response = {"message": "Grupo '%s'  encontrado, mas não foi modificado. "%(grupo["name"]) }
            return Response(dumps(response), status=400, content_type="application/json")
        else:
            response = {"message": "Grupo '%s'  não encontrado. "%(grupo["name"]) }
            return Response(dumps(response), status=404, content_type="application/json")

    except Exception as e:
        return "Erro: %s"%(e)



@grupos_routes.route("", methods=["POST"])
def postGrupos():
    try:
        grupo = request.get_json()
        mongo_db.grupo.insert_one(
            {
                "name" : grupo["name"],
                "integrantes" : []               
            }
        )
        response = {
            "message": "Grupo '%s' criado com sucesso!" %  (grupo["name"])
        }
        return Response(dumps(response), status=201, content_type="application/json")
    except Exception as e:
        return "Erro: %s " % (e)



@grupos_routes.route("")
def getGrupos():
    try:
        grupos = mongo_db.grupo.find()
        return Response(dumps(grupos), status=200, content_type="application/json")
    except Exception as e:
        return "Erro: %s"%(e)

    return "Lista de grupos"