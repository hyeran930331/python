
## 1. list
print(type(3)) #타입을 출력하는 것인가봄
myList =['재현', '혜영','정아']
print(type(myList)) #타입을 출력하는 것인가봄
print("\t myList[0], myList[2]:",myList[0], myList[2])
print("\t myList:",myList)

myTuple= ('재현27', '혜영27', '정아25')
print(type(myTuple)) #타입을 출력하는 것인가봄
print("\t myTuple:",myTuple)
# myTuple[0] = '김태훈'


mylist2 = [['최재현', '남', 27], ['남궁혜영','여',27], ['최정아','여',25]]
print("mylist2[0][1]:",mylist2[0][1])
for s in mylist2:
    print("\t mylist2: ",s)

## set
mySet = {'재현', '재현', '정아', '혜영'}
print("mySet :",mySet) #중복 x

# print(mySet[0])
for ms in mySet:
    print("\t ms:",ms)

##dict :키 값 java's map
student = {'name':'최재현','gender':'male','age':27}
print(student ['name'],student['age'])

db =[]
db.append({'name':'jeahyun', 'gender':'male','age':27})
# 안되구요. print(db['name'],db['age'])
db.append({'name':'junga', 'gender':'female','age':25})
db.append({'name':'teahun', 'gender':'male','age':27})
db.append({'name':'minjung', 'gender':'female','age':20})

for s in db:
    if s['age'] <= 25:
        print("25세이하:",s['name'])