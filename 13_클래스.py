# 섹션2-5강
# 클래스와 객체 세상에서 제일 쉽게 이해하기

# 클래스: 제품의 설계도
# 객체: 설계도로 만든 제품
# 속성: 클래스 안의 변수
# 메서드: 클래스 안의 함수
# 생성자: 객체를 만들 때 실행되는 함수
# 인스턴스: 메모리에 살아있는 객체


# 클래스 만들기
# class 클래스이름:
#     def 메서드이름(self):
#         명령블록

# 객체 = 클래스이름()
# 객체.메서드()

# 속성 추가하기
class Monster:
    def __init__(self, name, age):
        self.name = name # 속성
        self.age = age
    def say(self):
        print(f"나는 {self.name} {self.age}살임")

shark = Monster("상어", 7)
wolf = Monster("늑대", 3)

shark.say()
wolf.say()