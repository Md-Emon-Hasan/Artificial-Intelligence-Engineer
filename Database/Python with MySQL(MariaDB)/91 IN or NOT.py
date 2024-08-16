import pymysql as mq
mysql = mq.connect(host='localhost',user='root',passwd='',database='school')
mycursor = mysql.cursor()

print("{:<15} {:<15} {:<15}".format('Order ID','Order Date','Order Amount'))
try:
    sql = "Select order_id,order_date,order_amount from orders where order_id in(1,4)"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        print('{:<20} {:<20} {:<20}'.format(s[0],str(s[1]),s[2]))
except:
    print('Error...')