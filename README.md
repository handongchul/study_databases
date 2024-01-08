### mongoDB functions
- insertOne()|collection에 하나의 데이터(tyep = dictionary) 추가 |db.fruits.insertOne({...})
- insertMany()|collection에 여러 개의 데이터(type = list) 추가 |db.posts.insertMany({...})
- deleteOne()|collection에 Key = "Value"인 하나의 데이터 삭제 |db.fruits.deleteOne({ Key : "Value"})
- deleteMany()|collection에 Key = "Value"인 여러 개의 데이터 삭제 |db.fruits.deleteMany({Key : "Value"})
- deleteMany()|collection의 모든 데이터 삭제 |db.fruits.deleteMany({})
- find()|collection 내의 Key = Value인 데이터 검색|db.posts.find({}, {Key : "Value})

db.posts.find({category : {$eq : "Event"}},{title : 1,category:1,likes:1}) ;

db.posts.find({$and :[{category :{ $in : ["Event", "Tech"]}}, {likes:{$gt:4}}]}, {tilte:1, category:1, likes:1})

- $eq: ==
- $ne: !=
- $gt: >
- $gte: >=
- $lt: <
- $lte: <=
- $in: 다음 리스트에 포함된 값 중에 하나일 때/ {key : {$in : ["A","B"]}}
- $and: and / {$and :[{"조건"},{"조건"}]}
- $or: or / {$or :[{"조건"},{"조건"}]}
- $nor: nor / / {$nor :[{"조건"},{"조건"}]}
- $not: not 
- $inc: value의 수치를 증가시킬 때 사용하는 명령어 
- $rename: value의 이름을 바꿀 때 사용하는 명령어 
- $set: value를 추가할 때 사용하는 명령어
- $unset: value를 삭제할 때 사용하는 명령어 

