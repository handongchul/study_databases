class quest():
    def __init__(self,mongo_server_link,database_name):                                                                   # collection에 연결하는 함수 
        from pymongo import MongoClient
        self.mongoClient = MongoClient(mongo_server_link)                                                                 # mongo DB 서버에 연결
        self.database = self.mongoClient[database_name]                                                                   # 데이터 베이스에 연결
        self.todos_list = self.database["todos_list"]                                                                     # collection "todos_list"에 연결
        self.participants = self.database["participants"]                                                                 # collection "participants"에 연결
        self.participants_todo = self.database["participants_todo"]                                                       # collection "participants_todo"에 연결
        
    def todo_list_upload(self,list):    
        self.todos_list.delete_many({})                                                                                 
        self.todos_list.insert_many(list)                                                                                # todolist 업로드 
    
    def user_name_input(self):
        participate_dict = {}                                                                                      # 참여자의 dictionary 구성
        print("---------------------------------")
        str_participate =input("input Your Name : ")                                                               # 참여자의 이름 입력
        participate_dict["name"] =str_participate                                       
        self.participants.insert_one(participate_dict)                                                             # 참여자 리스트 업로드
        pass
        user_name = self.participants.find({},{"_id":1,"name":1})                                                  # 참여자의 이름과 ID  가져오기 
        list_user_name = ["",""]                                                                                   # user name 리스트 만들기 
        for i in user_name:
            list_user_name[0] = i["_id"]                                                                           # 첫번째 항목에 id 입력
            list_user_name[1] = i["name"]                                                                          # 두번쨰 항목에 이름 입력 
        return list_user_name


    def participate_todo(self):
        dict_todo = {}
        print("ToDo List 중 하나 선택 하세요 !")
        print("1. 주간 보고서 작성, 2. 이메일 확인 및 응답, 3. 회의 준비, 4. 프로젝트 계획서 수정, 5. 팀 멤버와의 1:1 면담")    # todolist 출력
        while True:                                                                                                    # 원하는 값이 입력될 때까지 반복 
            num_title = input("Title 번호 : ")                                                                         # title 번호 입력
            if num_title == "1" or num_title == "2" or num_title == "3" or num_title == "4" or num_title == "5":                           # 번호가 1,2,3,4 중 하나일 경우
                if num_title == "1":
                    str_title = "1. 주간 보고서 작성"
                elif num_title =="2":
                    str_title = "2. 이메일 확인 및 응답"
                elif num_title == "3":
                    str_title = "3. 회의 준비"
                elif num_title == "4":
                    str_title = "4. 프로젝트 계획서 수정"
                elif num_title == "5":
                    str_title = "5. 팀 멤버와의 1:1 면담"
                dict_todo["title"] = str_title                                                                         # dict_participate_todo 에 추가
                break                                                                                                  # 반복문 finish
            else:                                                                                                      # 아닐 경우
                print("'1','2','3','4','5' 중 하나를 입력해주세요.")                                                         # "'1','2','3','4' 중 하나를 입력해주세요." 출력 후, 반복
        while True:                                                                                                    # 원하는 값이 입력될 때까지 반복
            print("'완료' 또는 '진행중'을 입력해주세요.")
            str_status = input("Status : ")                                                                            # status 입력
            if str_status == "완료" or str_status == "진행중":                                                          # status 입력값이 '입력' 또는 '진행중'일 경우
                dict_todo["status"] = str_status                                                                       # dict_participate_todo에 추가
                break                                                                                                  # 반복문 finish
        return dict_todo

    def if_input_finish(self):     
        while True:                                                                                                   # 원하는 값이 나올 때까지 반복
            print("todo list 추가 시 'c', 다음 사용자 입력 시 'q', 모든 입력을 종료할 시 'x'를 입력하세요")
            input_finish = input("종료 여부 : ").lower()                                                               # 종료 여부 입력
            if input_finish == "c":                                                                                   # 종료 여부가 c 일 경우
                check_finish = "c"                                                                                    # check_finish = c로 지정
                break
            elif input_finish == "q":                                                                                 # 종료 여부가 q 일 경우
                check_finish = "q"                                                                                    # check_finish = q로 지정
                break
            elif input_finish == "x":                                                                                 # 종료 여부가 x 일 경우
                check_finish = "x"                                                                                    # check_finish = x로 지정
                break
        return check_finish

    def participants_todo_upload(self):
        self.participants.delete_many({})                                                                            
        self.participants_todo.delete_many({})
        while True:
            list_user_name = self.user_name_input()                                                                   # 참가자의 이름 입력
            while True:
                dict_participate_todo = {}
                dict_participate_todo["user_id"] = list_user_name[0]                                                  # dict_participate_todo에 id 입력 
                dict_participate_todo["user_name"] = list_user_name[1]                                                # dict_participate_todo에 name 입력
                dict_todo = self.participate_todo()                                                                   # todo list와 완료 여부 입력
                dict_participate_todo["title"] = dict_todo["title"]                                                   # dict_participate_todo에 todo list 입력
                dict_participate_todo["status"] = dict_todo["status"]                                                 # dict_participate_todo에 status 입력
                check_finish = self.if_input_finish()                                                                 # 종료 여부 입력
                pass
                if check_finish == "c":                                                                               # 종료 여부가 'c'일 경우 
                    self.participants_todo.insert_one(dict_participate_todo)                                          # participants_todo에 추가 후, 다시 dict_participate_todo 작성
                    pass
                else:                                                                                                 # 종료 여부가 'q'나 'x'일 경우
                    self.participants_todo.insert_one(dict_participate_todo)                                          # participants_todo에 추가 후, 참가자 이름부터 다시 입력
                    break
            pass
            list_user_name.clear()                                                                                    # 참가자 이름 초기화
            pass
            if check_finish =="x":                                                                                    # 종료 여부가 'x'일 경우
                break                                                                                                 # 함수 실행 종료
            pass

        print("---------------------------------")
        print("프로그램이 종료되었습니다.")
