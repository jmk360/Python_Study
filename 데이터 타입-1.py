# Section04-1
# 집합자료형 : List, Tuple, Dictionary, Set
# 데이터 타입

v_str1 = "Niceman"
v_bool = False
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25,
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_list))
print(type(v_tuple))
print(type(v_set))

i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999
big_int2 = 777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

# 파이썬 숫자형 및 연산자
"""
+ : 더하기
- : 빼기
* : 곱하기
/ : 나누기
// : 나누기(몫)
% : 나누기(나머지)
** : 지수(제곱)
단항 연산자
"""

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)

result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)

# 형변환
# int, float, comples(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

y = 100
# y = y + 100
# y += 100
y *= 100
print(y)

# 수치 연산 함수
# https://docs.python.org/3/library/math.html

print(abs(-7))
n, m = 10, 20
print(n, m)
n, m = divmod(100, 8)
print(n, m)

import math

print(math.ceil(5.1)) # 인수보다 크거나 같은 정수중 가장 작은 정수
print(math.floor(3.6)) # 인수보다 작거나 같은 정수중 가장 큰 정수