from fastapi import APIRouter, Response
from config.db import db
from schemas.titulo import tituloEntity, titulosEntity
from models.titulo import Titulo
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

titulo = APIRouter()

@titulo.get('/titulos')
async def find_all_titulos():
    tituloList = titulosEntity(db.titulos.find())
    return {"status": "ok", "data" : tituloList}

@titulo.post('/titulos')
async def create_titulo(titulo: Titulo):
    new_titulo = dict(titulo)
    new_titulo["password"] = sha256_crypt.encrypt(new_titulo["password"])
    # del new_titulo["id"]
    
    _id =db.titulos.insert_one(new_titulo)
    titulo = titulosEntity(db.titulos.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data" : titulo}


@titulo.get('/titulos/{id}')
async def find_titulo(id: str):
    titulo = titulosEntity(db.titulos.find({"_id":ObjectId(id)}))
    return {"status": "ok", "data" : titulo}
    

@titulo.put('/titulos/{id}')
def update_titulo(id: str, titulo: Titulo):
    db.titulos.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(titulo)})
    tituloReturn = dict(db.titulo.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": tituloReturn}

@titulo.delete('/titulos/{id}')
def delete_titulo(id: str):
    db.titulos.find_one_and_delete({"_id":ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)

