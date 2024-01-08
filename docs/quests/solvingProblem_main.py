import solvingProblem_functions

mongo_server_link = "mongodb://localhost:27017"                                                                       # mongoDB 서버 입력
database_name ="local"                                                                                                # 데이터 베이스 이름 입력
collection_name = 'solvingProblem'                                                                                    # collection 이름 입력

quiz_list = [                                                                                                        #추가할 리스트 작성
    {
        "question": "Python의 생성자 함수 이름은 무엇인가요?",
        "choices": ["__init__", "__main__", "__str__", "__del__"],
        "answer": "__init__",
        "answer_number":1,
        "score": 20
    },
    {
        "question": "Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?",
        "choices": ["print('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')", "echo 'Hello, World!'"],
        "answer": "print('Hello, World!')",
        "answer_number":1,
        "score": 20
    },
    {
        "question": "Python의 주석을 나타내는 기호는 무엇인가요?",
        "choices": ["//", "/* */", "#", "--"],
        "answer": "#",
        "answer_number":3,
        "score": 20
    },
    {
        "question": "Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?",
        "choices": ["size()", "length()", "len()", "sizeof()"],
        "answer": "len()",
        "answer_number":3,
        "score": 20
    },
    {
        "question": "Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?",
        "choices": ["str()", "int()", "char()", "float()"],
        "answer": "int()",
        "answer_number":2,
        "score": 20
    }
]

collection = solvingProblem_functions.connect(mongo_server_link,database_name,collection_name)                        # 추가하고자 하는 collection에 연결
collection.delete_many({})                                                                                            # 데이터 초기화
solvingProblem_functions.insert_list(collection,quiz_list)                                                            # 리스트 데이터 베이스에 추가
list_input = []                                                                                                       # 답안지 입력 리스트 
question_index = solvingProblem_functions.db_question(collection)                                                     # question 리스트 작성
choices_index = solvingProblem_functions.db_choices(collection)                                                       # choice 리스트 작성
answer_index = solvingProblem_functions.db_answer(collection)                                                         # answer 리스트 작성
answer_number_index = solvingProblem_functions.db_answer_number(collection)                                           # ansewr_number 리스트 작성
score_index = solvingProblem_functions.db_score(collection)                                                           # score 리스트 작성
str_user_name = solvingProblem_functions.user_name()                                                                  # 사용자 이름 입력
list_input = solvingProblem_functions.question_print(question_index,choices_index,answer_number_index,list_input)     # 질문지 출력과 답안지 입력 실행
solvingProblem_functions.score_sum(list_input,answer_number_index,score_index)                                        # 총점 출력
solvingProblem_functions.update_data(quiz_list,list_input,str_user_name,collection)                                   # 답안지 데이터 베이스에 저장