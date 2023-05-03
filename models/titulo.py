from pydantic import BaseModel

class Titulo(BaseModel):
    name: str 
    email: str 
    password: str
    