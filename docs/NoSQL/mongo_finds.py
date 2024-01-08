from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class 
# mongoClient = MongoClient("mongodb://localhost:27017")
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['posts']

# insert 작업 
documents = collection.find({}, {"_id": 1,"title":1,"likes":1})

# cast cursor to list 
list_documents =  list(documents)
print("list_documents length : {}".format(list_documents))
print(list_documents)
for document in documents:
    print("document: {}".format(document))
    pass
pass

documents.next()
