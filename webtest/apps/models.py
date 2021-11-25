from django.db import models

class fuser(models.Model):
    fname = models.CharField(max_length=20)
    fwork = models.CharField(max_length=150)
    fdollar = models.IntegerField(default=0)
    fsuccess = models.IntegerField(default=0)
    fjob = models.IntegerField(default=0)
    fcountry = models.CharField(max_length=50)
    fability1 = models.CharField(max_length=50)
    fability2 = models.CharField(max_length=50)
    fability3 = models.CharField(max_length=50)
    fability4 = models.CharField(max_length=50)
    
    def __str__(self):
        return self.fname



# # Connecting MySQL DB
# host = "127.0.0.1"
# port = 3306
# database = "qa"
# username = "root"
# password = "didrot1928"

# conn = pymysql.connect(user = username, passwd = password, host=host, db = database, port=port,use_unicode=True,charset='utf8')
# # cursor = conn.cursor()
# cursor = conn.cursor(pymysql.cursors.DictCursor)

# query = "SELECT * FROM Freelance_User"
# cursor.execute(query)
# result = cursor.fetchall()
# print(result[2]['id'])
# conn.close()

# class board:
#     def id(i):
#         return result[i]['id']
#     def name(i):
#         return result[i]['name']
#     def work(i):
#         return result[i]['work']
#     def dollar(i):
#         return result[i]['dollar']
#     def success(i):
#         return result[i]['success']
#     def job(i):
#         return result[i]['job']
#     def country(i):
#         return result[i]['country']
#     def abt1(i):
#         return result[i]['ability1']
#     def abt2(i):
#         return result[i]['ability2']
#     def abt3(i):
#         return result[i]['ability3']
#     def abt4(i):
#         return result[i]['ability4']


# query_clmn = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Freelance_User'"
# query_clmn = "DESC Freelance_User"
# cursor_clmn = conn.cursor()
# cursor_clmn.execute(query_clmn)
# result_clmn = cursor_clmn.fetchall()
# print(result_clmn)

# person0 = result[0] #데이터 내 사람 수(ROW)는 총 11명(줄) ~ 0번째부터 10번째까지
# name = person0[0] #항목(COLUMN)은 총 10개이고, 0번째항목이 name

## result[i] 일때, result[2]['id'] = 3
## 0 id
## 1 name
## 2 work
## 3 dollar
## 4 success
## 5 job
## 6 country
## 7 ability1
## 8 ability2
## 9 ability3
## 10 ability4

# class Board(models.Model):
#     b_name = models.AutoField(db_column='name')
#     b_work = models.AutoField(db_column='work')
#     b_dollar = models.AutoField(db_column='dollar')
#     b_success = models.AutoField(db_column='success')
#     b_job = models.AutoField(db_column='job')
#     b_country = models.AutoField(db_column='country')
#     b_ability1 = models.AutoField(db_column='ability1')
#     b_ability2 = models.AutoField(db_column='ability2')
#     b_ability3 = models.AutoField(db_column='ability3')
#     b_ability4 = models.AutoField(db_column='ability4')

# conn.commit() #입력하거나 변경할 경우 커밋(DB에 저장)

