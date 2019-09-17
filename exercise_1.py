import pymysql

db = pymysql.connect(host= 'localhost',
                     port= 3306,
                     user= 'root',
                     password= '123456',
                     database= 'dict',
                     charset= 'utf8')


cur = db.cursor()
f = open('dict.txt')

sql = 'insert into words (word,mean) values (%s,%s)'

for line in f:
    temp = line.split(' ',1)
    word = temp[0]
    mean = temp[1].strip()
    cur.execute(sql,[word,mean])
try:
    db.commit()
except Exception as e:
    print(e)
    db.rollback()


cur.close()
db.close()
