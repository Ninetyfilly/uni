from fastapi import APIRouter, Response
from config.db import db
from schemas.tramite import tramiteEntity, tramitesEntity
from models.tramite import Tramite
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

tramite = APIRouter()

@tramite.get('/tramites')
async def find_all_tramites():
    tramiteList = tramitesEntity(db.tramites.find())
    return {"status": "ok", "data" : tramiteList}

@tramite.post('/tramites')
async def create_tramite(tramite: Tramite):
    new_tramite = dict(tramite)
    new_tramite["password"] = sha256_crypt.encrypt(new_tramite["password"])
    # del new_tramite["id"]
    
    _id =db.tramites.insert_one(new_tramite)
    tramite = tramitesEntity(db.tramites.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data" : tramite}


@tramite.get('/tramites/{id}')
async def find_tramite(id: str):
    tramite = tramitesEntity(db.tramites.find({"_id":ObjectId(id)}))
    return {"status": "ok", "data" : tramite}
    

@tramite.put('/tramites/{id}')
def update_tramite(id: str, tramite: Tramite):
    db.tramites.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(tramite)})
    tramiteReturn = dict(db.tramite.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": tramiteReturn}

@tramite.delete('/tramites/{id}')
def delete_tramite(id: str):
    db.tramites.find_one_and_delete({"_id":ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)

