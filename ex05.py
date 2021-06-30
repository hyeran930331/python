import random# random 모듈을 로드한다. random.py파일을 로드한다
rsp = ['rock','sisor','paper']
num = int(random.random()*3) #0. 1, 2
sysChoice = num;2


myChoice = int(input('[0rock,1sisor,2paper] 0~2를 입력하세요 : '))
print('나:', rsp[myChoice])
print('시스템:', rsp[sysChoice])

me = rsp[myChoice]
com = rsp[sysChoice]

if me == com :
    print('same')
elif (com == 'rock' and me == 'paper') or (com =='sisoer' and me=='rock') or (com=='paper' and me=='sisoe'):
    print ('vic')
else :
    print ('lose')

if sysChoice == myChoice :
    print('same')
elif (myChoice-sysChoice <0) or (myChoice-sysChoice ==2) :
    print ('myChoice-sysChoice',myChoice,'-',sysChoice,'vic')
else :
    print ('myChoice-sysChoice',myChoice,'-',sysChoice,'lose')



    