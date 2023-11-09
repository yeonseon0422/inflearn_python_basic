# 섹션1-7강
# 프로그래밍의 꽃, 반복문 - for while 사용법 익히기

# for: 정한 횟수만큼 반복
# while: 조건을 만족하지 않을 때까지 반복

# for
# for 변수 in 리스트:
#     명령블록

for a in [1, 2, 3, 4]:
    print(a)
    
# 예제1
coffees = ['Americano', 'latte', 'cappuccino']
for coffee in coffees:
    print(coffee)

# 반복 횟수를 정해주고 싶을 때 : range()
# range(시작, 끝+1, 단계)
for i in range(60):
    print(i + 1, "분")

for i in range(1, 11, 2):
    print(i, "번째 페이지입니다.")
    
    
# while
# 아래는 같은 결과를 나타냄

for count in range(5):
    print(count, "번째 반복입니다.")

count = 0
while count < 5:
    print(count, "번째 반복입니다.")
    count = count + 1