# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서 o, 중복 o, 수정 o, 삭제 o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(d[0:1])
print(d[0:2])
print(e[2][1:3])

print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c) # [77, 2, 3, 4]

c[1:2] = [100, 1000, 10000]
print(c) # [77, 100, 1000, 10000, 3, 4]
c[1] = ['a', 'b', 'c']
print(c) # [77, ['a', 'b', 'c'], 1000, 10000, 3, 4] 

# del 키워드 사용
del c[1] 
print(c) # [77, 1000, 10000, 3, 4] 

del c[-1]
print(c) # [77, 1000, 10000, 3]

print()
print()
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7)
print(y)

# del 은 인덱스를 가지고 지우지만, remove 일때는 값을 가지고 지운다.
y.remove(2)
y.remove(7)
print(y)

# pop 은 맨마지막을 꺼낸다음에 return 한다. 
# # LIFO
print(y.pop()) 
print(y)

print(y.pop(1))
print(y)

ex = [88, 77]
y.extend(ex)
print(y)

y.append(ex)
print(y)

# 삭제 : del, remove, pop
# pop을 계속 사용하면 언젠가는 error가 난다.

d = [1,2,3]
d.pop()
d.pop()
d.pop()
# d.pop() # IndexError 발생한다.

# 튜플 (순서 o, 중복 o, 수정 x, 삭제 x)

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# del c[2] # tuple 은 삭제 할 수 없다.

print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)

print()
print()

# 튜플 함수

z = (5, 1, 1, 3, 4)
print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))