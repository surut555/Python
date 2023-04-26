import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",passwd="")
    cs = con.cursor()
    cs.execute("CREATE DATABASE register ")
except pymysql.err.OperationalError:
    print("ไม่สามารถสร้างฐานข้อมูลได้")
except pymysql.ProgrammingError:
    print("คำสั่ง SQL ไม่ถูกต้อง !!")

else:
    print("สร้างฐานข้อมูลเรียบร้อยแล้ว")
    con.close()
    cs.close()