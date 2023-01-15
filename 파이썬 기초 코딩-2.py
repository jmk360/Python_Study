# Section02-2

import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My name is Goodboy!')

# 변수 선언
myName = "Goodboy"

# 조건문
if myName == "Goodboy":
    print('ok')

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('{} * {} = {}'.format(i, j, i * j))
    print('-'*10)

print()

for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d =' %(i, j), i*j)
    print('-'*10)

# 변수 선언(한글)
이름 = "좋은사람"

# 출력
print(이름)

# 함수 선언(한글)
def 인사():
    print('안녕하세요. 반갑습니다.')

인사()

# 함수 선언(영문)
def greeting():
    print('Hello!')

# 출력
greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
