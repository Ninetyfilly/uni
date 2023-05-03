def estadisticaEntity(estadistica) -> dict:
    return {
        "id": str(estadistica["_id"]),
        "name": estadistica["name"],
        "email":estadistica["email"],
        "password": estadistica["password"]
    }
    
def estadisticasEntity(estadisticas) -> list:
    return [estadisticaEntity(item) for item in estadisticas]