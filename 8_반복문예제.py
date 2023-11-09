# 섹션1-8강
# 파이썬 반복문 예제 3문제 풀어봅시다


# 예제1) 프로그램 사용자로부터 자연수를 입력 받고, 0부터 자연수까지의 합계를 출력하세요.

# input_number = int(input("자연수를 입력하세요 >>> "))
# total_number = 0

# for i in range(1, input_number + 1):
#     total_number = total_number + i

# print(total_number)


# 예제2) 사용자로부터 -1을 입력 받으면 프로그램이 종료되는 프로그램을 작성해보세요.

# 방법1
# print("프로그램 시작")

# num = int(input("종료하려면 -1을 입력하세요: "))

# while num != -1:
#     num = int(input("종료하려면 -1을 입력하세요: "))

# print("프로그램 종료")

# 방법2
# print("프로그램 시작")

# while True:
#     num = int(input("종료하려면 -1을 입력하세요: "))
#     if num == -1:
#         break

# print("프로그램 종료")


# 예제3)

while True:
    print("[메뉴를 입력하세요]")
    select = int(input("1. 게임시작 2. 랭킹보기 3. 게임종료 >>> "))
    if select == 1:
        print("-> 게임을 시작합니다")
    elif select == 2:
        print("-> 랭킹보기")
    elif select == 3:
        print("-> 게임을 종료합니다")
        break
    else:
        print("-> 다시 입력해 주세요")