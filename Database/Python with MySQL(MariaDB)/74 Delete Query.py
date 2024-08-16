import pymysql as mq
mysql = mq.connect(host='localhost',user='root',passwd='',database='school')
cursorobj = mysql.cursor()
st_id = input('Enter The Student ID: ')
sql = 'DELETE From student where st_id=%s'
try:
    cursorobj.execute(sql,st_id)
    mysql.commit()
    print('Student DELETED')
except:
    print('Error')