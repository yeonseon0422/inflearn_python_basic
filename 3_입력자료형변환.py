# 섹션1-3강
# 입력과 자료형변환 간단하게 정리하기

# 입력함수: input()
# 자료형변환
# 문자->숫자: int(), 숫자->문자: str()


# 예제1) 사용자로부터 숫자를 입력받아 곱한 값 출력하기

x = int(input("숫자를 입력하세요 >>> "))
y = int(input("곱할 숫자를 입력하세요 >>> "))

print(x * y)


# 예제2) 사용자로부터 연도를 입력받아 현재 나이 출력하기

year = int(input("태어난 연도를 입력하세요 >>> "))
age = 2023 - year + 1

print(str(age) + "세 입니다!")