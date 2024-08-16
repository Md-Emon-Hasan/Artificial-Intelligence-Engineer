import pymysql as mq
mysql = mq.connect(host='localhost',user='root',passwd='',database='school')
mycursor = mysql.cursor()

print('{:<15} {:<20} {:<20}'.format('st_name','st_class','st_email'))

try:
    # sql = 'Select * from student order by st_name DESC'
    # using limit
    # sql = 'Select * from student order by st_name DESC LIMIT 0,2'
    sql = 'Select * from student order by st_name DESC LIMIT 1,2'
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print('{:<15} {:<20} {:<20}'.format(s[0],s[1],s[2]))
except:
    print('Error...')