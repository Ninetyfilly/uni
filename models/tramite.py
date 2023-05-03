from pydantic import BaseModel

class Tramite(BaseModel):
    name: str 
    email: str 
    password: str
    