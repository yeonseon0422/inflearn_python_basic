# 섹션2-2강
# 파이썬 로또 예상 번호 만들기

# 1. 로또 번호 6개를 생성
# 2. 로또 번호는 1~45까지의 랜덤한 번호
# 3. 6개의 숫자 모두 달라야 한다
# 4. 로또 번호 생성함수를 작성하고 사용한다

import random

# 내가 푼 답

def getLottoNumbers(a):
    numbers = []
    i = 0
           
    while i < a:
        number = random.randint(1, 45)
        if number not in numbers:
            numbers.append(number)
            i = i + 1
    
    return numbers

print(getLottoNumbers(6))


# 정답 코드

lotto_num = []

def getRandomNumber():
    number = random.randint(1, 45)
    return number

# 중복 포함
# for i in range(6):
#     random_number = getRandomNumber()
#     print(random_number)

count = 0

while True:
    if count > 5:
        break
    random_number = getRandomNumber()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count = count + 1
        
print(lotto_num)