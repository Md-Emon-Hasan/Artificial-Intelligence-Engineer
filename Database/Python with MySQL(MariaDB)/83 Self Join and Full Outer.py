import pymysql as mq
db = mq.connect(host='localhost',user='root',passwd='',database='school')
cur = db.cursor()

try:
    sql = "SELECT * from cat as c1, cat as c2 where c1.cat_id=c2.parent_id"
    cur.execute(sql)
    sdata = cur.fetchall()
    for a in sdata:
        print(a)
except:
    pass