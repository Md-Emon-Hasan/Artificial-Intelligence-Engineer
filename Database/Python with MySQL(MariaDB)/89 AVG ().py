import pymysql as mq
mysql = mq.connect(host='localhost',user='root',passwd='',database='school')
mycursor = mysql.cursor()

print("{:<15} ".format('Order Avg'))
try:
    sql='Select avg(order_amount) from orders'
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print('{:<15}'.format(s[0]))
except:
    print('Error...')