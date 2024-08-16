import pymysql as mq
mysql = mq.connect(host='localhost',user='root',passwd='',database='school')
mycursor = mysql.cursor()

print('{:<15} {:<20} '.format('State ID','State Name'))
try:
    sql = 'Select state_id, state_name from state where state_id between 2 and 5'
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print("{:<15} {:<20}".format(s[0],s[1]))
except:
    print('Error')