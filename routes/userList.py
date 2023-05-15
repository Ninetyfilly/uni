from fastapi import APIRouter, Response
from config.db import db
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

@user.get('/users')
async def find_all_users():
    try:
        userList = usersEntity(db.users.find())
        return {"status": "ok", "data" : userList}
    except Exception:
            # código que maneja el error
            return {"status": "error", "data" : 'user not found'}

@user.post('/users')
async def create_user(user: User):
    try:
        new_user = dict(user)
        # new_user["password"] = sha256_crypt.encrypt(new_user["password"])
        # del new_user["id"]
        
        _id =db.users.insert_one(new_user)
        user = usersEntity(db.users.find({"_id": _id.inserted_id}))
        return {"status": "ok", "data" : user}
    except Exception:
        # código que maneja el error
        return {"status": "error", "data" : 'user not found'}


@user.get('/users/{id}')
async def find_user(id: str):
    try:
        user = usersEntity(db.users.find({"_id":ObjectId(id)}))
        return {"status": "ok", "data" : user}
    except Exception:
        # código que maneja el error
        return {"status": "error", "data" : 'user not found'}
    

@user.put('/users/{id}')
def update_user(id: str, user: User):
    try:
        db.users.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
        userReturn = dict(db.user.find({"_id": ObjectId(id)}))
        return {"status": "ok", "data": userReturn}
    except Exception:
        # código que maneja el error
        return {"status": "error", "data" : 'user not found'}

@user.delete('/users/{id}')
def delete_user(id: str):
    try:
        db.users.find_one_and_delete({"_id":ObjectId(id)})
        return Response(status_code=HTTP_204_NO_CONTENT)
    except Exception:
        # código que maneja el error
        return {"status": "error", "data" : 'user not found'}

@user.post('/login')
def login_user(user: User):
    try:
        userLogin = usersEntity(db.users.find({"username": user.username}))
        login = dict(userLogin[0])
        print(login.get("id", "error"))
        return {"status": "ok", "data" : 'log In'}
    except Exception:
        # código que maneja el error
        return {"status": "error", "data" : 'user not found'}

