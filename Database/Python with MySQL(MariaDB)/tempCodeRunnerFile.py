sql = "Select order_id,order_date,order_amount from orders where order_id in(1,6)"
mycursor.execute(sql)
sdata = mycursor.fetchall()
for s in sdata:
    print('{:>15} {:<15} {:<15}'.format(s[0]),str(s[1]),s([2]))