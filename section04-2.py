# Section04-2
# 문자열, 문자열 연산, 슬라이싱

str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ''
str4 = ' '
str5 = str()
str6 = str('abc')

print(len(str1), len(str2), len(str3), len(str4), len(str5), len(str6))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab \t Tab \t"
print(escape_str2)
print('aaaaaaaabbbbbbbbccccccccddddddd')

# Raw String : escape string이 적용되지 않는다.
raw_s1 = r"\n\n\n"
raw_s2 = r"C:\Programs\Test\Bin"
raw_s3 = r'\\a\\a'
print(raw_s1)
print(raw_s2)
print(raw_s3)

# 멀티라인(Multi Line)
multi = """ 문자열 멀티라인 테스트"""
print(multi)

multi = \
"""
문자열

멀티라인

테스트
"""

print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
# print(str_o1 + 3) # TypeError
print(str_o1 * 3)
print(str_o4)
print('a' in str_o4)
print('f' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
print(str(77) + 'a')
print(str(10.4))

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

a = 'niceman'
b = 'orange'
c = 'dave.py'

print(a.islower())
print(a.endswith('a'))
print(c.endswith(".py"))
print(a.capitalize())
print(a.replace('nice', 'good'))
print(reversed(b))
print(list(reversed(b)))

# 문자열은 한번 할당이 되면 변경이 불가능하다.

a = 'niceman'
b = 'orange'

print(a[0:3])
print(a[0:4])
print(a[0:7])
print(a[0:])
print(a[:])
print(a[0:len(a)])
print(b[0:4])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])