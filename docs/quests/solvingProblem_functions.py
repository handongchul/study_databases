def connect(mongo_server_link,database_name,collection_name):                                                   # collection에 연결하는 함수 작성
    from pymongo import MongoClient
    mongoClient = MongoClient(mongo_server_link)                                                                # mongo DB 서버에 연결
    database = mongoClient[database_name]                                                                       # 데이터 베이스에 연결
    collection = database[collection_name]                                                                      # collection에 연결
    return collection

def insert_list(collection,list_items):                                                                         # 리스트의 dict들을 모두 추가하는 함수 작성
    for i in range(len(list_items)):                                                                            # 리스트의 dict들이 모두 추가될 때까지 반복
        dict_quiz = list_items[i]                                              
        collection.insert_one(dict_quiz)                                                                            # 리스트의 dict 추가

def user_answer(collection,list_items,user_name):                                                                         # 리스트의 dict들을 모두 추가하는 함수 작성
    for i in range(len(list_items)):                                                                            # 리스트의 dict들이 모두 추가될 때까지 반복
        dict_quiz = list_items[i][user_name]                                              
        collection.insert_one(dict_quiz)
def db_question(collection):                                                                                              # collection에서 question 데이터를 가져와 리스트 작성
    quiz = collection.find({},{"_id":0,"question":1, "choices":1,"answer":1,"answer_number":1,"score":1})
    list_question = []   
    for i in quiz:
        list_question.append(i["question"])
    return list_question
def db_choices(collection):                                                                                               # collection에서 choice 데이터를 가져와 리스트 작성
    quiz = collection.find({},{"_id":0,"question":1, "choices":1,"answer":1,"answer_number":1,"score":1})
    list_choices = []   
    for i in quiz:
        list_choices.append(i["choices"])
    return list_choices
def db_answer(collection):                                                                                                # collection에서answer 데이터를 가져와 리스트 작성
    quiz = collection.find({},{"_id":0,"question":1, "choices":1,"answer":1,"answer_number":1,"score":1})
    list_answer = []   
    for i in quiz:
        list_answer.append(i["answer"])
    return list_answer 
def db_answer_number(collection):                                                                                         # collection에서 answer_number 데이터를 가져와 리스트 작성
    quiz = collection.find({},{"_id":0,"question":1, "choices":1,"answer":1,"answer_number":1,"score":1})
    list_answer_number = []   
    for i in quiz:
        list_answer_number.append(i["answer_number"])
    return list_answer_number
def db_score(collection):                                                                                         # collection에서 answer_number 데이터를 가져와 리스트 작성
    quiz = collection.find({},{"_id":0,"question":1, "choices":1,"answer":1,"answer_number":1,"score":1})
    list_score = []   
    for i in quiz:
        list_score.append(i["score"])
    return list_score
def user_name():                                                                                                # 사용자 이름 입력
    user_name = input("사용자 이름:")
    return user_name

def question_print(list_question, list_choices,list_answer_number,list_input):                                  # 질문지 출력과 정답 입력 프린트
    for i in range(len(list_question)):
        print("-------------------------------------")                                                 
        print(list_question[i])
        for j in range(len(list_choices[i])):
            print("{}. {} ".format(j+1,list_choices[i][j]))
        input_answer = int(input("답을 입력하세요.:"))
        if int(input_answer) == list_answer_number[i]:
            print("정답입니다!")
        else:
            print("오답입니다.")
        list_input.append(input_answer)
    return list_input

def score_sum(list_input,list_answer_number,list_score):                                                      # 최종 점수 출력 함수 작성
    score_sum = 0
    for i in range(len(list_input)):
        if list_input[i] == list_answer_number[i]:
            score_sum = score_sum + list_score[i]
    print("==========================================")
    print("최종 점수 : {}".format(score_sum))
    return score_sum

def update_data(quiz_list,list_input,user_name,collection):
    for i in range(len(quiz_list)):                                                                            # 답안지를 작성자의 이름의 key로 데이터 저장
        quiz_list[i][user_name] = list_input[i]
    for i in range(len(quiz_list)):
        collection.update_one({"question": quiz_list[i]["question"]},{'$set': {user_name : list_input[i]}})