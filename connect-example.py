import pymysql
dbcon=pymysql.connect(host='localhost', port=3306, user='root', passwd='', charset='utf8', db='ifoodly')#資料庫資訊
a=[1,2,3,4]
b=['a','b','c']
with dbcon.cursor() as cursor:
    sql= 'insert into member (ID, Name) values (%s ,%s);'#sql指令
    for i in range(0,3):
        cursor.execute(sql, (a[i], b[i]))#執行sql指令
    dbcon.commit()#提交至sql
dbcon.close()#關閉資料庫