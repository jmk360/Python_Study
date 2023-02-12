# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is : ", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is : ", v2)

for v3 in range(1, 11):
    print("v3 is ", v3)

# 1 ~ 100 합
# 방법1
i = 1
isum = 0
while i <= 100:
    isum += i
    i += 1
print("1 ~ 100 합 =", isum)

# 방법2
isum = 0
for i in range(1, 101):
    isum += i
print("1 ~ 100 합 =", isum)

# 방법3
print("1 ~ 100 합 =", sum(range(1,101)))
print('1 ~ 100 의 짝수의 합 =', sum(range(0,101,2)))

# 시퀀스(순서 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable : range, reversed, enumerate, map, zip

names = ["Kim", "Park", "cho", "Choi", "Yoo"]

for name in names:
    print("You are : ", name)

word = "dreams"

for s in word:
    print("Word : ", s)

my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul"
}

# 키
for key in my_info:
    print('my_info : ', key)

# 값
for v in my_info.values():
    print('my_info : ', v)

# 키
for key in my_info.keys():
    print('my_info : ', key)

# 키, 값
for k, v in my_info.items():
    print(k, v)
   
# 대문자는 소문자로, 소문자는 대문자로 바꾸시오.
name = "KennRY"
for n in name:
    if n.isupper():
        print(n.lower(), end='')
    else:
        print(n.upper(), end='')
print()

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : 33!")

# for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : 33!")
else:
    print("Not found 33....")

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is float:
        continue
    print("타입 : ", type(v))