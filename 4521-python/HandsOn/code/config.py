from pymongo import MongoClient

mongo_con = MongoClient()
mongo_db = mongo_con["flask-app"]



""" inserted = mongo_db.user.insert_one(
     {
         "name": "usuario_nome",
         "email": "usuario_email",
         "messages": [
             {
                 "name": "usuario_nome",
                 "message": "mensagem"
             }
         ]
     }
 )
print(inserted) """