# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#    code 

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요 : 함수 선언은 함수 호출보다 위에 있어야 한다.

# 예제1
def hello(world):
    print("Hello", world)

hello("Python")
hello(7777)

# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!!!")
print(str)

# 예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)
print(type(val1), type(val2), type(val3))

# 예제4(데이터 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))

# 예제4-1
def func_mul3(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

tp = func_mul3(100)
print(tp, type(tp))

# 예제5
# *args, *kwargs

def args_func(*args):
    print(type(args))
    print(args)
    for t in args:
        print(t)

args_func("kim")
args_func("kim", "park")
args_func("kim", "park", 'Lee')

print()

def args_func2(*args):
    for i, v in enumerate(args):
        print(i, v)

args_func2("kim")
args_func2("kim", "park")
args_func2("kim", "park", 'Lee')

def args_func3(*args):
    for i, v in enumerate(range(10)):
        print(i, v)

args_func3()

# kwargs
def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1="Kim")
kwargs_func(name1="Kim", name2="Park", name3="Lee")

def kwargs_func2(**kwargs):
    for k, v in kwargs.items():
        print(k ,v)

kwargs_func2(name1="Kim")
kwargs_func2(name1="Kim", name2="Park", name3="Lee")

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim')
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)

# 중첩함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)

# 예제6(hint) : hint를 명시적으로 사용하면 함수를 사용할때 이 함수의 입력 타입과 출력타입을 알 수 가 있다.
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5.0))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))

lambda_mul_10 = lambda num: num * 10

print(">>>", lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x: x * 1000))