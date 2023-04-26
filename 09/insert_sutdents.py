import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",passwd="",db="register")
    cs = con.cursor()
    cs.execute("""INSERT INTO students (student_id,	f_name,	l_name,	e_mail,	tel) 
                                VALUES (10001,"นายกานต์","เรียนเก่ง","kan@gmail.com","098457634"),
                                        (10002,"นางสาวพรพิมล","ขยันเรียน","pornpmon@gmail.com","0984563745")""")
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