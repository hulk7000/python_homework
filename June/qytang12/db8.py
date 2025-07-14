import sqlite3
conn = sqlite3.connect('qytangdb1.sqlite')
cursor = conn.cursor()
cursor.execute('create table test(t1 int, t2 varchar(40))')
cursor.execute("insert into test(t1,t2) values(11, 'welcome to qytang')")
cursor.execute("insert into test(t1,t2) values(12, 'welcome to python')")
cursor.execute("insert into test(t1,t2) values(13, 'welcome to FRanK')")
cursor.execute("select * from test")
yourresult = cursor.fetchall()
for i in yourresult:
    print(i)
conn.commit()