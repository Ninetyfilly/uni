from fastapi import APIRouter, Response
from config.db import db
from schemas.estadistica import estadisticaEntity, estadisticasEntity
from models.estadistica import Estadistica
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

estadistica = APIRouter()

@estadistica.get('/estadisticas')
async def find_all_estadisticas():
    estadisticaList = estadisticasEntity(db.estadisticas.find())
    return {"status": "ok", "data" : estadisticaList}

@estadistica.post('/estadisticas')
async def create_estadistica(estadistica: Estadistica):
    new_estadistica = dict(estadistica)
    new_estadistica["password"] = sha256_crypt.encrypt(new_estadistica["password"])
    # del new_estadistica["id"]
    
    _id =db.estadisticas.insert_one(new_estadistica)
    estadistica = estadisticasEntity(db.estadisticas.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data" : estadistica}


@estadistica.get('/estadisticas/{id}')
async def find_estadistica(id: str):
    estadistica = estadisticasEntity(db.estadisticas.find({"_id":ObjectId(id)}))
    return {"status": "ok", "data" : estadistica}
    

@estadistica.put('/estadisticas/{id}')
def update_estadistica(id: str, estadistica: Estadistica):
    db.estadisticas.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(estadistica)})
    estadisticaReturn = dict(db.estadistica.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": estadisticaReturn}

@estadistica.delete('/estadisticas/{id}')
def delete_estadistica(id: str):
    db.estadisticas.find_one_and_delete({"_id":ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)

