import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",passwd="",db="register")
    cs = con.cursor()
    cs.execute("""INSERT INTO registers (student_id,	subject_id,	semester, register_data) 
                                VALUES (10001, 101, 1, 20230423)""")
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