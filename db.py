from tinydb import TinyDB
db =TinyDB("db.json", indent =4)
db.insert({"user_id":5,"username":"user1"})
db.insert({"user_id":8,"username":"user3"})