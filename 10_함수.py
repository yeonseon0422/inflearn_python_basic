# 섹션2-1강
# 파이썬 함수 def 정의하고 호출하기

# 함수(function): 작업을 수행하는 명령블록

# def 함수이름(매개변수):
#     명령블록
#     ...
#     return 리턴값

# 매개변수가 있는 함수
# 덧셈함수 만들어보기
def sum (a, b):
    result = a + b
    return result

x = sum(1, 2)
y = sum(3, 4)

print(x)
print(y)


# 매개변수가 없는 함수
# def 함수이름():
#     명령블록
#     ...
#     return 리턴값

import random

def getRandomNumber():
    number = random.randint(1, 10)
    return number

print(getRandomNumber())


# 리턴값이 없는 함수
# def 함수이름(매개변수):
#     명령블록
#     ...
    
def printName(name):
    print(name)

print(printName("안녕"))    
    
    
# 매개변수와 리턴값이 없는 함수
# def 함수이름():
#     명령블록
#     ...
    
def sayHi():
    print("안녕하세요")

sayHi()