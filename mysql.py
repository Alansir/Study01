import pymysql

db = pymysql.connect(host = 'localhost',port = 3306,user = 'root',passwd = ' ',database = 'stu',charset = 'utf8')

cur = db.cursor()
cur.execute("insert into myclass values (7,'Emma',11,'w',86.5);")

db.commit()

cur.close()
db.close()