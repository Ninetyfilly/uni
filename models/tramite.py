from pydantic import BaseModel
from datetime import date
from typing import Optional

class Tramite(BaseModel):
    NoConsec: Optional[int]
    fojasTotales: int
    folioInit: int
    folioFin: int
    asunto: str
    # fechaAper: date
    # fechaCierre: date
    
    class Config:
        # Especificar el formato de fecha esperado para la entrada y la validación
        anystr_strip_whitespace = True
        datetime_format = "iso"  # Formato ISO 8601 YYYY-MM-DD
    