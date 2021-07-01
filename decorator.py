def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()


def decorator_function(original_function):  #1함수선언
    def wrapper_function():  #5 함수선언
        return original_function()  #7 받았던 인자값의 함수를 실행
    return wrapper_function  #6 함수실행

def display():  #2 함수선언 자바에서 public void sum(){ 같은 
    print('display 함수가 실행됐습니다.')  #8 실행.

decorated_display = decorator_function(display)  #3
#ecorated_display라는 변수에 display 함수를 인자로 갖은 
# decorator_function을 실행한 리턴값을 할당

decorated_display()  #4 decorated_display()를 통해 wrapper_function을 호출



#30-49
def decorator_function(original_function):
    def wrapper_function():
        print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
        return original_function()
    return wrapper_function

def display_1():
    print('display_1 함수가 실행됐습니다.')

def display_2():
    print('display_2 함수가 실행됐습니다.')

display_1 = decorator_function(display_1)  #1
display_2 = decorator_function(display_2)  #2

display_1()
print
display_2()

#50-66 
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):  #1
        print ('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
        return original_function(*args, **kwargs)  #2
    return wrapper_function

@decorator_function
def display():
    print ('display 함수가 실행됐습니다.')

@decorator_function
def display_info(name, age):
    print 'display_info({}, {}) 함수가 실행됐습니다.'.format(name, age)

display()
print
display_info('John', 25)