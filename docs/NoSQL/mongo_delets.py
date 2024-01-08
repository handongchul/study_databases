from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class 
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['fruits']

# insert 작업 진행
fruit_infor = [
    {"name": "사과", "color": "빨강", "taste": "달콤"},
    {"name": "바나나", "color": "노랑", "taste": "달콤"},
    {"name": "포도", "color": "보라", "taste": "달콤한데 약간의 쓴맛이 있음"},
    {"name": "오렌지", "color": "주황", "taste": "달콤하면서 새콤"}
]

insert_result = collection.insert_many(fruit_infor)

list_inserted_ids = insert_result.inserted_ids

# delete inserted records by _ids
collection.delete_many({"_id":list_inserted_ids[0]})
pass

