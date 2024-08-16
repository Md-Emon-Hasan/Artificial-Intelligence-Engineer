import pymysql as mq
mysql = mq.connect(host='localhost',user='root',passwd='',database='school')
mycursor = mysql.cursor()
try:
    #st_id, st_name, st_class, st_email
    ins = 'INSERT INTO student(st_name,st_class,st_email) values(%s,%s,%s)'
    t = ('ravi','12th','ram@gmail.com')
    mycursor.execute(ins,t)
    mysql.commit();
    print('Insert Data')
except:
    print('Error...')
    
# adding multiple row
# try:
#     ins = 'INSERT INTO student(st_name,st_class,st_email) values(%s,%s,%s)'
#     t = [('raj','10th','raj@gmail.com'),('testing','10th','testing@gmail.com')]
#     mycursor.executemany(ins,t)
#     mysql.commit();
#     print('Insert Data')
# except:
#     print('Error...')