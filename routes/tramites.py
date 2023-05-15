from fastapi import APIRouter, Response
from config.db import db
from schemas.tramite import tramiteEntity, tramitesEntity
from models.tramite import Tramite
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
import datetime
from bson import BSON

tramite = APIRouter()

@tramite.get('/tramites')
async def find_all_tramites():
    try:
        tramiteList = tramitesEntity(db.tramites.find())
        return {"status": "ok", "data" : tramiteList}
    except Exception:
            # código que maneja el error
            return {"status": "error", "data" : 'user not found'}

@tramite.post('/tramites')
async def create_tramite(tramite: Tramite):
    try:
        new_tramite = dict(tramite)
        tramiteList = len(tramitesEntity(db.tramites.find()))
        new_tramite["NoConsec"] = tramiteList + 1
        print('new_tramite',new_tramite)
        _id = db.tramites.insert_one(new_tramite)
        new_tramite = tramitesEntity(db.tramites.find({"_id": _id.inserted_id}))
        return {"status": "ok", "data" : new_tramite}
    except Exception:
            # código que maneja el error
            return {"status": "error", "data" : 'problem in tramites'}


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

