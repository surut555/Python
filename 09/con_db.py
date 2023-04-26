import pymysql
con = pymysql.connect(host="localhost",user="root",passwd="",db="")
cs = con.cursor()
cs.execute("show databases")
sv = cs.fetchall()
print(sv)
con.close()
cs.close()