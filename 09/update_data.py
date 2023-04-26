import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",passwd="", db="register", charset="utf8")
    cs = con.cursor()
    cs.execute(""" UPDATE subjects SET subject_name = 'การเขียนโปรแกรมด้วยภาษา Python' 
                    WHERE subject_id = '109' """)
    con.commit()
    con.close()
    cs.close()
except pymysql.err.OperationalError:
    print("ไม่สามารถติดต่อฐานข้อมูลได้")
except pymysql.err.ProgrammingError:
    print("คำสั่ง SQL ไม่ถูกต้อง")
    con.rollback()
else:
    print("ปรับปรุงข้อมูลสำเร็จ")