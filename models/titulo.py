from pydantic import BaseModel

class Titulo(BaseModel):
    localizacion: str 
    folio: str 
    # fechaDeElabo: str
    nombreTitu: str
    nombreBenefi: str
    noLote: str
    ubicacion: str
    libro: str
    foja: str
    folioTramite: str
    
    
    
    