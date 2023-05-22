def tituloEntity(titulo) -> dict:
    return {
        "id": str(titulo["_id"]),
        "localizacion": titulo["localizacion"],
        "folio":titulo["folio"],
        # "fechaDeElabo": titulo["fechaDeElabo"],
        "nombreTitu": titulo["nombreTitu"],
        "nombreBenefi": titulo["nombreBenefi"],
        "noLote": titulo["noLote"],
        "ubicacion": titulo["ubicacion"],
        "libro": titulo["libro"],
        "foja": titulo["foja"],
        "folioTramite": titulo["folioTramite"],
    }
    
def titulosEntity(titulos) -> list:
    return [tituloEntity(item) for item in titulos]