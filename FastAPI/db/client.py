from pymongo import MongoClient

#Base de datos local
db_client = MongoClient().local

#Base de datos remota
#db_client = MongoClient("mongodb+srv://toralsergio23:<password>@test.o4a02t8.mongodb.net/?retryWrites=true&w=majority").prueba
