def tramiteEntity(tramite) -> dict:
    return {
        "id": str(tramite["_id"]),
        "name": tramite["name"],
        "email":tramite["email"],
        "password": tramite["password"]
    }
    
def tramitesEntity(tramites) -> list:
    return [tramiteEntity(item) for item in tramites]