import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",passwd="",db="register")
    cs = con.cursor()
    cs.execute("""INSERT INTO subjects (subject_id, subject_name, unit, teacher_id) 
                                VALUES (110,"Information Technologies", 3, 103)""")
except pymysql.err.OperationalError:
    print("ไม่สามารถติดต่อฐานข้อมูลได้")
except pymysql.err.ProgrammingError:
    print("คุณเขียนคำสั่ง SQL ผิดพลาด")
    con.rollback()
else:
    con.commit()
    print("บันทึกข้อมูลเรียบร้อย")
    con.close()
    cs.close()