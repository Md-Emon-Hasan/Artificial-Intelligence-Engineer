import pymysql as mq
mysql = mq.connect(host='localhost',user='root',passwd='',database='school')
mycursor = mysql.cursor()

print('{:<15} {:<20} {:<20}'.format('Student ID','Student Name','Student Class','Student Email'))
try:
    # using filter
    # name = input('Enter the Student Name:- ')
    # sql = "Select * from Student where st_name = '"+name+"'"
    
    # for searching
    # name = input('Enter the student name:- ')
    # sql = "Select * from student where st_name like '%"+name+"%'"
    
    name = input('Enter the student name:- ')
    Classname = input('Enter the student class name:- ')
    sql = "Select * from student where st_name like '%"+name+"%' and st_class = '"+Classname+"'"

    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print('{:<15} {:<20} {:<20}'.format(s[0],s[1],s[2],s[3]))
except:
    print('Error...')