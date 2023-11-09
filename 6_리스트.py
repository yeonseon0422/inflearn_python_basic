# 섹션1-6강
# 여러 개의 데이터를 저장할 수 있는 자료형, 리스트에 대해 알아보자

# 리스트명 = [데이터, 데이터, ..., 데이터]
# 리스트명[인덱스]

# 리스트 생성하기
animals = ["사자", "호랑이", "고양이", "강아지"]
print(animals)

# 데이터 접근하기
name = animals[0]
print(name)

# 데이터 추가하기
# 리스트명.append(데이터)
animals.append("햄스터")
animals.append(1) # 리스트는 데이터 타입이 달라도 됨
print(animals)

# 데이터 삭제하기
# del 리스트명[인덱스]
del animals[-1] # -1은 마지막 데이터를 의미함
print(animals)

# 리스트 슬라이싱
# 리스트[시작:끝+1]
print(animals[0:3])

# 리스트 길이
# len(리스트)
print(len(animals))

# 리스트 정렬
# 리스트.sort() : 기본 오름차순으로 정렬됨
animals.sort()
print(animals)

animals.sort(reverse=True) # 내림차순 정렬
print(animals)