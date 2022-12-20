# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value(Json) -> MongoDB
# 선언

a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': 870214}
b = {0: 'Hello Python', 1: "Hello Coding"}
c = {'arr': [1, 2, 3, 4, 5]}

print(type(a))

# 출력
print(a['name'])
# print(a['name1']) # KeyError 발생한다.
print(a.get('name'))
print(a.get('name1')) # get 함수는 key가 없으면 none을 return 한다. 그냥하는 것보다 좀더 안전하다.
print(a.get('address'))

print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3,)
print(a)

# Keys, Values, Items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(list(a.items()))
print(1 in b)
print(2 in b)
print('name' in a)
print("name2" in a)

# 집합(Sets) (순서x, 중복x)
#  : 수치계산, 과학 연산 에 많이 사용된다.

a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5 ,6, 6])
d = {1, 2, 3, 4}

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1.intersection(s2))
print(s1 & s2)

# 합집합
print(s1.union(s2))
print(s1 | s2)

# 차집합
print(s1.difference(s2))
print(s1 - s2)

# 추가 & 제거
s3 = {7, 8, 10, 15}
s3.add(18)
print(s3)
s3.add(7)
print(s3)

s3.remove(15)
print(s3)

print(type(s3))