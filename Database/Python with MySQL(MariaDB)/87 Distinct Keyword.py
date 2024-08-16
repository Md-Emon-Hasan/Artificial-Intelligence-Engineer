import pymysql as mq
mysql = mq.connect(host='localhost',user='root',passwd='',database='school')
mycursor = mysql.cursor()

# print("{:<15} {:<15} {:<15}".format('Emp Id','Emp Name','Emp DName'))
# try:
#     sql = 'Select empno,ename,dname from operators'
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall()
#     for s in sdata:
#         print("{:<15} {:<15} {:<15}".format(s[0],str(s[1]),s[2]))
# except:
#     print('Error..')

print("{:<15}".format('Emp DName'))
try:
    sql = 'Select distinct(dname) from operators'
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print("{:<15}".format(s[0]))
except:
    print('Error..')