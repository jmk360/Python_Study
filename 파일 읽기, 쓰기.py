# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print()
print(dir(f))
# 반드시 close 리소스 반환
f.close()

print('-' * 20)
print('-' * 20)

# 예제2
# with문은 close를 생략해도 된다.
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print('-' * 20)
print('-' * 20)

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip()) # print(c, end='')
        

print('-' * 20)
print('-' * 20)

# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 내용 없음
    print(">", content) 

print('-' * 20)
print('-' * 20)

# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line.strip()) # print(line, end='')
        line = f.readline()

print('-' * 20)
print('-' * 20)

# 예제6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    print()
    for c in contents:
        print(c.strip())

print('-' * 20)
print('-' * 20)

# 예제7
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    print()
    for c in contents:
        print(c.strip())

print('-' * 20)
print('-' * 20)

# 예제8 -> 강사님이 짠 코드
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)
print('점수 합 = {}'.format(sum(score)))
print('점수 평균 = {:6.3f}'.format(sum(score) / len(score)))

print('-' * 20)
print('-' * 20)

# 예제8 -> 내가 짠 코드
scores = list()
with open('./resource/score.txt', 'r') as f:
    scores = f.readlines()
    scores = [int(score.strip()) for score in scores]
sum_scores = sum(scores)
avg_scores = sum_scores / len(scores)
print('점수 합 = {}'.format(sum_scores))
print('점수 평균 = {}'.format(avg_scores))

# 파일 쓰기

# 예제1
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman!\n')

# 예제2
with open('./resource/text1.txt', 'a') as f:
    f.write('Goodman!\n')

# 예제3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)

# 예제5
# print문을 활용해서 파일 쓰기도 가능하다.
# 많이 사용되지는 않지만 알고 있는 것이 좋다.
with open('./resource/text4.txt', 'w') as f:
    print('Test Contests1!', file=f)

print('-'*20)

# encoding='utf-8' 해당 옵션을 주지 않으면 한글 쓰기가 안된다.
with open('./resource/test.log', 'w', encoding='utf-8') as f:
    print('hi! dave', file=f)
    f.write('안녕하세요\n')