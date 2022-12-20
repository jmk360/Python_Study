# SEction07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 선언
# class 클래스명:
#     함수
#     함수
#     함수

# 예제1
class UserInfo:
    # 속성, 메소드 : 클래스는 속성과 메소드로 구성된다.
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)

user1 = UserInfo("Kim")
user1.user_info_p()