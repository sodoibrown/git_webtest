from django.db import connection, models
# import pymysql

class cuser(models.Model):
    cname = models.CharField(max_length=50)
    cage = models.IntegerField(default=0)
    ccountry = models.CharField(max_length=50)
    def __str__(self):
        return self.cname
class fuser:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Freelance_User")
    rst = cursor.fetchall()

    cursor1 = connection.cursor()
    cursor1.execute("SELECT id FROM Freelance_User")
    fid = cursor1.fetchall()

    cursor2 = connection.cursor()
    cursor2.execute("SELECT name FROM Freelance_User")
    fname = cursor2.fetchall()

    # cursor3 = connection.cursor()
    # cursor3.execute("SELECT work FROM Freelance_User")
    # fwork = cursor3.fetchall()

    # cursor4 = connection.cursor()
    # cursor4.execute("SELECT dollar FROM Freelance_User")
    # fdollar = cursor4.fetchall()

    # cursor5 = connection.cursor()
    # cursor5.execute("SELECT success FROM Freelance_User")
    # fsuccess = cursor5.fetchall()

    # cursor6 = connection.cursor()
    # cursor6.execute("SELECT job FROM Freelance_User")
    # fjob = cursor6.fetchall()

    # cursor7 = connection.cursor()
    # cursor7.execute("SELECT country FROM Freelance_User")
    # fcountry = cursor7.fetchall()

    # cursor8 = connection.cursor()
    # cursor8.execute("SELECT ability1 FROM Freelance_User")
    # fabt1 = cursor8.fetchall()

    # cursor9 = connection.cursor()
    # cursor9.execute("SELECT ability2 FROM Freelance_User")
    # fabt2 = cursor9.fetchall()

    # cursor10 = connection.cursor()
    # cursor10.execute("SELECT ability3 FROM Freelance_User")
    # fabt3 = cursor10.fetchall()

    # cursor11 = connection.cursor()
    # cursor11.execute("SELECT ability4 FROM Freelance_User")
    # fabt4 = cursor11.fetchall()

    # for i in range(len(rst)):
    #     id =  rst[i]['id']
    #     name = rst[i]['name']
    #     work =  rst[i]['work']
    #     dollar =  rst[i]['dollar']
    #     success = rst[i]['success']
    #     job =  rst[i]['job']
    #     country = rst[i]['country']
    #     abt1 = rst[i]['ability1']
    #     abt2 = rst[i]['ability2']
    #     abt3 = rst[i]['ability3']
    #     abt4 = rst[i]['ability4']

    # connection.close()
