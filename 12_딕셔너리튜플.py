# 섹션2-3강
# 딕셔너리와 튜플

# 딕셔너리: 키와 값의 쌍으로 이루어진 자료형
# 딕셔너리이름 = {키1:값1, 키2:값2, ...}

play_data = {
    'result' : '승리',
    'champ_name' : '비에고',
    'kill' : 13,
    'death' : 9,
    'assist' : 17
}

# 딕셔너리 접근법
print(play_data['result'])

# 딕셔너리 수정법
# 기존 값 변경
play_data['result'] = '패배'

# 새로운 키, 값 추가
play_data['lever'] = 18

# 데이터 삭제
del play_data['champ_name']

print(play_data)


# 딕셔너리 관련 함수: keys(), values(), items()

# keys()
for key in play_data.keys():
    print(key)
    
# values()
for value in play_data.values():
    print(value)
    
# items()
for key, value in play_data.items():
    print(key, value)
    
    
# 튜플(tuple): 값을 바꿀 수 없는 리스트

tuple_a = (1, 2, 3, 4)

tuple_a[0] = 2 # 접근만 가능, 수정은 불가!