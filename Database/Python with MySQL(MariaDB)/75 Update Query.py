import pymysql as mq
mysql = mq.connect(host='localhost',user='root',passwd='',database='school')
cursorobj = mysql.cursor()
name = input('Enter the student name:- ')
class_name = input('Enter the class name:- ')
st_email = input('Enter the email:- ')
st_id = input('Enter the student ID:- ')

sql = 'UPDATE student set st_name = %s,st_class = %s,st_email = %s where st_id = %s'
data = (name,class_name,st_email,st_id)

try:
    cursorobj.execute(sql,data)
    mysql.commit()
    print('Data Uploaded')
except:
    print('Error...')
