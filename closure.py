#프로그래밍 언어에서의 클로저란 퍼스트클래스 함수를 지원하는 언어의 네임 바인딩 기술이다
#클로저는 어떤 함수를 함수 자신이 가지고 있는 환경과 함께 저장한 레코드이다
#함수가 가진 프리변수(free variable)를 클로저가 만들어지는 당시의 값과 레퍼런스에 맵핑하여 주는 역할을 한다

def outer_func(): #1 함수선언
    message='Hi' #3 함수가 호출되면 message에 문자열 할당

    def inner_func(): #4 함수선언
        print(message) #6 함수가 호출되면 message를 출력한다.
        # 여기서 message는 inner_func 안에서 정의되지는 않았지만, 
        # inner_func 안에서 사용되기 때문에 프리변수라고 부릅니다.
    #return inner_func() #5함수 호출
    return inner_func 

outer_func() #2함수 호출 
#return inner_func()입력시 결과 : Hi 
#return inner_func 으로 입력시 결과 : 아무변화 없음.= inner_func를 할당
my_func = outer_func() # 리턴값인 inner_func를 변수에 할당합니다.
print(my_func)  #할당 확인 결과:<function outer_func.<locals>.inner_func at 0x000001CE07B00CA0>
my_func() #inner_func 실행 결과: Hi

# my_func=inner_func 함수가 outer_func 함수의 로컬변수인 message를 참조했다. 
# 로저는 함수의 프리변수 값을 어딘가에 저장한다고 했던것 같습니다. 도데체 어디에 저장을 하는 걸까요?

print(dir(my_func)) #  dir() 명령어를 이용해 my_func의 네임스페이스를 확인 결과 :'__closure__'
print(type(my_func.__closure__)) #__closure__는 무슨 타입 결과 :<class 'tuple'>
print(my_func.__closure__[0] ) #튜플안에 첫 번째 아이템입니다. 
#결과: <cell at 0x000001A765282FD0: str object at 0x000001A764DE8D70>"cell"이라는 문자열 오브젝트네요.
print(dir(my_func.__closure__[0])) # 이 cell 오브젝트는 어떤 속성들을 가지고 있을까요
print(my_func.__closure__[0].cell_contents) #cell_contents에는 뭐가 들어 있는지 확인 해 보겠습니다.  결과 : Hi


#클로저는 이렇게 하나의 함수로 여러가지의 함수를 간단히 만들어낼 수 있게도 해주며, 
# 기존에 만들어진 함수나 모듈등을 수정하지 않고도 
# wrapper 함수를 이용해 커스터마이징할 수 있게 해주는 기특한 녀석입니다.

