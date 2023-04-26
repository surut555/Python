import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",passwd="",db="register")
    cs = con.cursor()
    cs.execute("""INSERT INTO teachers (teacher_id,	f_name,	l_name,	e_mail,	tel) 
                                VALUES (1001,"นายรติ","สอนดี","rati@gmail.com","0895976874"),
                                        (102,"นางภาพร","ขยันสอน","kanok@gmail.com","0986754678")""")
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