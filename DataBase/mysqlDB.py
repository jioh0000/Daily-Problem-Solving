import pymysql

conn = pymysql.connect(host='localhost', user='testuser', password='password!@', db='testdb', charset='utf8')

sql = "SHOW DATABASES"

with conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        for data in cur:
            print(data)