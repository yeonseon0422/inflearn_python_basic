# 섹션1-5강
# 조건문 예제를 통한 프로그래밍 실력 업그레이드

# 예제1)
# 프로그램 사용자로부터 삼성전자의 현재가격을 입력 받는다
# 1. 현재가격이 9만원 이상이면 -> "매도합니다" 출력
# 2. 현재가격이 8만원 이상, 9만원 미만이면 -> "대기중입니다" 출력
# 3. 현재가격이 8만원 미만이면 -> "매수합니다" 출력

price = int(input("삼성전자의 현재가격을 입력하세요 >>> "))

if price >= 90000:
    print("매도합니다")
elif price >= 80000:
    print("대기중입니다")
else:
    print("매수합니다")
    
    
# 예제2)
# 프로그램 사용자로부터 가방과 시계의 금액을 입력 받는다
# 1. 합계금액이 10만원 이상이면 할인률 30%
# 2. 합계금액이 5만원 이상 10만원 미만이면 할인률 20%
# 3. 합계금액이 5만원 미만이면 할인률 10%

bag_price = int(input("가방 금액을 입력하세요 >>> "))
watch_price = int(input("시계 금액을 입력하세요 >>> "))
total_price = bag_price + watch_price

# if total_price >= 100000:
#     print("금액은" + str(total_price*0.7) + "입니다.")
# elif total_price >= 50000:
#     print("금액은" + str(total_price*0.8) + "입니다.")
# else:
#     print("금액은" + str(total_price*0.9) + "입니다.")
    
# 답안
if total_price >= 100000:
    total_price = total_price * 0.7
elif total_price >= 50000:
    total_price = total_price * 0.8
else:
    total_price = total_price * 0.9

print("합계 금액은 :", total_price)
    