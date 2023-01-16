# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ', nowDatetime)

# sqlite3
print('sqlite3.version : ', sqlite3.version) # sqlite 버전
print('sqlite3.sqlite_version : ', sqlite3.sqlite_version) # sqlite 엔진 버전

# DB 생성 & Auto Commit(Rollback)
conn = sqlite3.connect('C:/dave/fastcampus/Coding_Algorithem/python_basic/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor type : ', type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
# c.execute("INSERT INTO users VALUES(1, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.com', ?)", (nowDatetime,)) # ?는 튜플 형태로 매칭시켜야 한다.
# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)", (2, 'Park', 'Park@daum.net', '010-1111-1111', 'Park.com', nowDatetime))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@daum.net', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@google.com', '010-4444-4444', 'Yoo.net', nowDatetime)
)

# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)", userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영(오토 커밋) 
# -> 만약에 이 옵션을 사용하지 않았다면, conn.commit() 함수를 직접 실행해 주어야 반영이된다.
# -> conn.rollback() 함수를 통해서 롤백 : 반영이 된것을 되돌린다.

# 접속 해제
conn.close()