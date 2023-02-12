# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

# print('Test)

# if True
#     pass

# x => y

# NameError : 참조변수 없음

# a = 10
# b = 15
# print(c)

# ZeroDivisionError : 0 나누기 에러

# print(10 / 0)

# IndexError : 인덱스 범위 오버
# x = [10, 20, 30]
# print(x[0])
# print(x[3]) # 예외 발생

# KeyError

dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}

# print(dic['hobby'])
# print(dic.get('hobby')) # 딕셔너리에서 키를 조회 할때는 다이렉트로 접근하지 말고 안전하게 get 함수를 사용하는 것을 권장한다.

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 에러

# import time
# print(time.time())
# print(time.month())

# ValueError : 참조 값이 없을 때 발생

x = [1, 5, 9]

# x.remove(10)
# x.index(10)

# FileNotFoundError

# f = open('test.txt', 'r') # 예외 발생

# TypeError

x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y) # 예외
# print(x + z) # 예외

# print(x + list(y)) # 예외 발생 안함

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim' # Cho 예외발생
    x = name.index(z)
    print('{} Found it! in name : {}'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('OK! else!')

# 예제2
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it! in name : {}'.format(z, x+1))
except: # 예외가 어떤게 나올지 모를경우 그냥 except로 처리를 하면 된다.
    print('Not found it! - Occurred Eror!')
else:
    print('OK! else!')

print()
print()

# 예제3
# 예를 들어 외부의 프로그램을 연결하는 stream 작업을 했다면, 에러가 발생하든, 발생하지 않든 그 연결을 끊어주는 작업을 처리
# 할때와 같이 무조건 적인 처리를 할때는 finally를 사용한다.

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name : {}'.format(z, x+1))
except: # 예외가 어떤게 나올지 모를경우 그냥 except로 처리를 하면 된다.
    print('Not found it! - Occurred Eror!')
else:
    print('OK! else!')
finally:
    print('finally ok!')

# 예제4
# 파이썬 코드에서 많이 보이는 패턴 : 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally:
    print('ok Finally!!!!')

# 예제5
name = ['Kim', 'Lee', 'Park']
# except 는 계층적으로 예상가능한 예외처리를 하되 Exception는 마지막에 와야한다. Exception을 맨 위에다가 놓으면
# 모든 에러가 Exception에 걸린다.
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name : {}'.format(z, x+1))
except ValueError as l: # alias 사용가능하다.
    print(l)
    print('Not found it! - Occurred ValueEror!')
except IndexError:
    print('Not found it! - Occurred IndexEror!')
except Exception:
    print('Not found it! - Occurred Eror!')
else:
    print('OK! else!')
finally:
    print('finally ok!')

# 예제6
# 예외 발생 : raise # 파이썬에서 예외발생할 수 있지만, 내가 임의적으로 예외를 발생시킬 수 도 있다.
# raise 키워드로 예외 직접 발생 -> 고급 프로그래밍을 하기위해서는 이런것도 할 줄 알아야 한다.

try:
    a = 'Kim'
    if a == 'Kim':
        print('Ok 허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('OK!')

print()
print()

# 강의에서는 다루지 않았지만, 파이썬 사용자 정의 예외처리 에 대해서 개인적으로 공부를 하자!!

# 사용자 정의 예외 처리
# 사용 예시1
class Example1Error(Exception):
    pass

def sample1_func():
    try:
        if True:
            raise Example1Error
    except Example1Error:
        print("Example1Error 발생")

sample1_func()   

print()
print()

# 사용 예시2
class Example2Error(Exception):
    def __init__(self):
        super().__init__("Example2Error 발생")

def sample2_func():
    try:
        if True:
            raise Example2Error
    except Example2Error as e:
        print(e)

sample2_func()

print()
print()


# 사용 예시3
class Example3Error(Exception):
    def __init__(self, a):
        super().__init__(a)

def sample3_func():
    try:
        if True:
            raise Example3Error("Example3Error 발생")
    except Example3Error as e:
        print(e)

sample3_func()

print()
print()

# 사용 예시4
class Example4Error(Exception):
    def __init__(self, a):
        self._a = a
    def __str__(self): # __repr__(self) 로 사용해도 됨
        return self._a

def sample4_func():
    try:
        if True:
            raise Example4Error("Example4Error 발생")
    except Example4Error as e:
        print(e)

sample4_func()   