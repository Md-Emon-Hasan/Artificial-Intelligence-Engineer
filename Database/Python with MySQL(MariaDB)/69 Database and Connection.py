import pymysql as mq
# server name --> localhost
# username --> root
# password --> ''
myobj = mq.connect(host="localhost", user="root", password="")
cursorobj = myobj.cursor()

try:
    db = 'create database school'
    cursorobj.execute(db)
    print('database created')
except:
    print('database error...')