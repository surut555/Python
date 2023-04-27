import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",passwd="")
    cs = con.cursor()
    cs.execute("drop database register")
    con.close()
    cs.close()
except pymysql.err.OperationalError:
    print("ไม่สามารถติดต่อฐานข้อมูลดได้ !!!")
except pymysql.err.ProgrammingError:
    print("คำสั่ง SQL ไม่ถูกต้อง !!")
else:
    print("ลบฐานข้อมูลสำเร็จ")