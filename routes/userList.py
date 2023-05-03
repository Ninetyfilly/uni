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
    userList = usersEntity(db.users.find())
    return {"status": "ok", "data" : userList}

@user.post('/users')
async def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    # del new_user["id"]
    
    _id =db.users.insert_one(new_user)
    user = usersEntity(db.users.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data" : user}


@user.get('/users/{id}')
async def find_user(id: str):
    user = usersEntity(db.users.find({"_id":ObjectId(id)}))
    return {"status": "ok", "data" : user}
    

@user.put('/users/{id}')
def update_user(id: str, user: User):
    db.users.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    userReturn = dict(db.user.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": userReturn}

@user.delete('/users/{id}')
def delete_user(id: str):
    db.users.find_one_and_delete({"_id":ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.post('/login')
def login_user(user: User):
    login = dict(user)
    print('login',login)
    userLogin = usersEntity(db.users.find({"name": user.name}))
    if(userLogin._id):
        return {"status": "ok", "data" : 'log In'}
    else:
        return {"status": "error", "data" : 'user not found'}
        

