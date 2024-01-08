from pymongo import MongoClient

def connect(mongo_server_link,database_name,collection_name):                # collection에 연결하는 함수 작성
    mongoClient = MongoClient(mongo_server_link)                             # mongo DB 서버에 연결
    database = mongoClient[database_name]                                    # 데이터 베이스에 연결
    collection = database[collection_name]                                   # collection에 연결
    return collection

def insert_list(collection,list_items):                                                    #리스트의 dict들을 모두 추가하는 함수 작성
    for i in range(len(list_items)):                                            # 리스트의 dict들이 모두 추가될 때까지 반복
        dict_fruit = list_items[i]                                              
        collection.insert_one(dict_fruit)                                        # 리스트의 dict 추가

fruit_info = [                                                         #추가할 리스트 작성
    {"name": "사과", "color": "빨강", "taste": "달콤"},
    {"name": "바나나", "color": "노랑", "taste": "달콤"},
    {"name": "포도", "color": "보라", "taste": "달콤한데 약간의 쓴맛이 있음"},
    {"name": "오렌지", "color": "주황", "taste": "달콤하면서 새콤"}
]

mongo_server_link = "mongodb://localhost:27017"                                 # mongoDB 서버 입력
database_name ="local"                                                          # 데이터 베이스 이름 입력
collection_name = 'fruits_info'                                                 # collection 이름 입력

collection = connect(mongo_server_link,database_name,collection_name)                        # 추가하고자 하는 collection에 연결
insert_list(collection,fruit_info)