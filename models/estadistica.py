from pydantic import BaseModel

class Estadistica(BaseModel):
    name: str 
    email: str 
    password: str
    