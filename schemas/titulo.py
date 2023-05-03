def tituloEntity(titulo) -> dict:
    return {
        "id": str(titulo["_id"]),
        "name": titulo["name"],
        "email":titulo["email"],
        "password": titulo["password"]
    }
    
def titulosEntity(titulos) -> list:
    return [tituloEntity(item) for item in titulos]