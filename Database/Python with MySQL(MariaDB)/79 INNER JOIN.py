import pymysql as mq
mysql = mq.connect(host='localhost',user='root',passwd='',database='school')
mycursor = mysql.cursor()

# print('{:<15} {:<20} {:<20}'.format('State ID','State Name','Country ID'))

print('{:<15} {:<20} {:<20}'.format('State ID','State Name','Country Name'))

try:
    # sql = 'Select * from state inner join country on state.country_id = country.country_id'
    
    sql = 'Select state.state_id, state.state_name, country.country_name from state inner join country on state.country_id = country.country_id'
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print("{:<15} {:<20} {:<20}".format(s[0],s[1],s[2]))
except:
    print('Error...')