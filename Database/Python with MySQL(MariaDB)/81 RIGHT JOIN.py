import pymysql as mq
mysql = mq.connect(host='localhost',user='root',passwd='',database='school')
mycursor = mysql.cursor()

print("{:<15} {:<20} {:<20} {:<20} {:<20}".format("User ID","User Name",'User Address','Order ID','Order Amount'))

try:
    sql = "Select user.user_id,user.user_name,user.user_address,orders.order_id, orders.order_amount from user right join orders on user.user_id=orders.user_id"
    
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print('{:<15} {:<20} {:<20} {:<20}'.format(s[0],s[1],s[2],s[3],s[4]))
except:
    print('Error...')