from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from routes.userList import user
from routes.tramites import tramite
from routes.titulos import titulo
from routes.estadisticas import estadistica


# control+shift+ñ

# python -m uvicorn main:app --reload
# http://127.0.0.1:8000


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173"
]



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(tramite)
app.include_router(titulo)
app.include_router(estadistica)




class DatosBasicos(BaseModel):
    nombre: str
    documento1: str
    documento2: str

@app.get("/")
def index():
    dato = 45
    dato2 = "string"
    dato3 = 1000
    data = {
        "dato" : dato,
        "dato 2" : dato2,
        "dato 3" : dato3 
    }
    return {"message": "alaverga", "data": data}
        



