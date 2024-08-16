# select quary
import pymysql as mq
# server connection or database connection
mysql = mq.connect(host='localhost',user='root',passwd='',database='school')
mycursor = mysql.cursor()
print('{:<20} {:<20} {:20} {:10}'.format('Student ID','Student Name','Student Email','Student Class'))
try:
    # see specifc data
    # sql = 'Select st_id,st_name from student where st_id=2'
    
    sql = 'Select * from student'
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    
    # fetchone function
    # fetchone use for single line showing data
    # sdata = mycursor.fetchone()
    # print('{:<15} {:<20}'.format(sdata[0],sdata[1]))
    # for s in sdata:
    #     print(s)
    
    # string format
    for s in sdata:
        print('{:<20} {:<20} {:<20} {:<20}'.format(s[0],s[1],s[2],s[3]))
    # show specific data
    for s in sdata:
        print('{:<20} {:<20}'.format(s[0],s[1]))
except:
    print('Error...')