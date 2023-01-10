# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모 

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color
    
    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        # super(tp, color) # 왜 이렇게 하면 에러가 나오는지는 모르겠지만, 이렇게 사용하지 않고, 위 방식처럼 부모의 속성을 초기화한다.
        self.car_name = car_name

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name

    def show(self):
        print(super().show()) # super() 키워드를 통해서 부모의 속성이나 메소드를 사용할 수 있다.
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__)

# Method Overriding(오버라이딩)
model2 = BenzCar("220d", 'suv', 'black')
print(model2.show())

# Parent Method Call
model3 = BenzCar('350s', 'sedan', 'silver')
print(model3.show())

# Inheritance Info
# __mro__, mro() : 클래스의 상속 관계를 알려준다. / 소스를 파악할때 자주 사용한다. / 상속정보를 리스트로 반환한다.
print(BmwCar.__mro__)
print(BmwCar.mro()) 
print(BenzCar.mro()) 

# 예제2
# 다중 상속
# 너무나 많은 다중 상속은 코드를 해석하기가 어려울 수 있다.
# 보통 복잡한거 할때는 2개정도 상속을 받는다.
# 상속의 depth가 너무 깊으면 복잡하다. -> 복잡도가 높지않게, 상속을 적절하게 사용해야 한다.
class X():
    pass

class Y():
    pass
    
class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
print(A.mro())