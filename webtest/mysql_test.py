host = "localhost"
port = 3306
database = "qa"
username = "root"
password = "didrot1928"

import pymysql

conn = pymysql.connect(user = username, passwd = password, host=host, db = database, port=port,use_unicode=True,charset='utf8')
cursor = conn.cursor()

query = "SELECT * FROM Freelance_User"
cursor.execute(query)
result = cursor.fetchall()

for i in result:
    print(i[0])

