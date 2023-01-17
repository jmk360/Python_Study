# Section12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

import sqlite3

# DB생성(파일)
conn = sqlite3.connect('./resource/database.db')

# Cursor 연결
c = conn.cursor()

# 데이터 수정1
# c.execute("update users set username = ? where id = ?", ('niceman', 2))

# 데이터 수정2 # 주의 => =: 와 컬럼명 사이에 스페이스가 들어가면 에러가 난다.
# c.execute("update users set username =:name where id =:id", {'name': 'goodman', 'id': 5})

# 데이터 수정3
# c.execute("update users set username = '%s' where id = '%s'" %('badboy', 3))

# 중간 데이터 확인1
for user in c.execute("select * from users"):
    print(user)

# Row Delete1
c.execute("delete from users where id = ?", (2,))

# Row Delete2
c.execute("delete from users where id =:id", {"id": 5})

# Row Delete3
c.execute("delete from users where id = '%s'" % 4)

print()

# 중간 데이터 확인2
for user in c.execute("select * from users"):
    print(user)

# 테이블 전체 데이터 삭제
print("users db deleted : ", conn.execute("delete from users").rowcount, " rows")

# 커밋
conn.commit()

# 접속 해제
conn.close()