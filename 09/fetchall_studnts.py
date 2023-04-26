import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",passwd="",db="register")
    cs = con.cursor()
    cs.execute("SELECT * FROM students")
except pymysql.err.OperationalError:
    print("ไม่สามารถติดต่อฐานข้อมูลได้")
except pymysql.err.ProgrammingError:
    print("คุณเขียนคำสั่ง SQL ผิดพลาด")
    con.rollback()
else:
    data = cs.fetchall()
    for i in data:
        print(i)
    con.close()
    cs.close()