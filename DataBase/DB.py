#CRUD
    # Create
    # Read
    # Update
    # 

import sqlite3

# DB 파일 열기
conn = sqlite3.connect("chinook.db")
# print(conn) 하면 주소값이 나온다

# Cursor 생성
cursor = conn.cursor()
# 커서로 어느 db로 힐지 가르킨다

# SQL 명령어
CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS Lol(
        id integer primary key autoincrement,   
        champion text not null,
        ward text not null,
        jungleMob text
    );
"""
# primary key -> 주민등록번호 같이 겹치지 않는 값
# autoincrement -> 1 부터 n까지 1씩 늘어난다
# not null -> null 값이 있으면 안된다

# SQL 명령 실행
cursor.execute(CREATE_SQL)

# CHECK
cursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='Lol';")
table_list = cursor.fetchall()

for i in table_list:
    for j in i:
        print(j)

# INSERT SQL 작성
INSERT_SQL = 'INSERT INTO Lol(champion, ward, jungleMob) VALUES(?,?,?);'

# 데이터 여러개 한 번에 넣기
data = (
    ('Ezreal', 'Pink', "두꺼비"),
    ('Acali', 'Lens', "칼부"),
    ('Katarina', 'Pink', "블루")
)

cursor.executemany(INSERT_SQL, data)
# 데이터베이스에 반영 시키기
conn.commit()

cursor.execute('SELECT * FROM Lol;')
item_list = cursor.fetchall()
for i in item_list:
    print(i)

# Table 삭제하기
# conn.execute('DROP TABLE Lol')

# DELETE 일부 행만 삭제하기
query = """
    DELETE FROM Lol
        WHERE (name='ward);
"""

# UPDATE = 기존에 있던 값들을 변경하고 싶을때
query = """
    UPDATE Lol SET champoin='Rulu' where champion='Ezreal';
"""

conn.execute(query)
conn.commit()

# READ
cursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='Lol';")
table_list = cursor.fetchall()

for i in table_list:
    for j in i:
        print(j)

# DB Close
conn.close()