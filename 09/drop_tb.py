import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",passwd="",db="register", charset="utf8")
    cs = con.cursor()
    cs.execute("drop table registers")
    con.commit()
    con.close()
    cs.close()
except pymysql.err.OperationalError:
    print("ไม่สามารถเชื่อมต่อฐานข้อมูลได้ !!!")
    con.rollback()
except pymysql.err.ProgrammingError:
    print("คำสั่ง SQL ไม่ถูกต้อง !!!")
else:
    print("ลบตารางสำเร็จ")