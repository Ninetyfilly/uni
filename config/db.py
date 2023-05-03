from pymongo  import MongoClient

conn = MongoClient("mongodb+srv://proyecto:contra1234@proyectoin.wy3jpic.mongodb.net/?retryWrites=true&w=majority")

db = conn.panteones

# users = db["users"]
# print(users)