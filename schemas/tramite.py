def tramiteEntity(tramite) -> dict:
    return {
        "id": str(tramite["_id"]),
        "NoConsec": tramite["NoConsec"],
        "fojasTotales":tramite["fojasTotales"],
        "folioInit": tramite["folioInit"],
        "folioFin": tramite["folioFin"],
        "asunto": tramite["asunto"],
        # "fechaAper": tramite["fechaAper"],
        # "fechaCierre": tramite["fechaCierre"],
    }
    
def tramitesEntity(tramites) -> list:
    return [tramiteEntity(item) for item in tramites]