import pymysql

db = pymysql.connect(host='10.6.0.103',
user='root',password='123456',database='sys')

cursor = db.cursor()

cursor.execute('SELECT VERSION()')


DATA = cursor.fetchone()

print(DATA)

db.close()


