import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",passwd="",database="register")
    cs = con.cursor()
    #ตารางนักเรียน
    cs.execute(""" CREATE TABLE students (student_id INT (5) NOT NULL,
                                        f_name CHAR (30) COLLATE utf8_bin,
                                        l_name CHAR (30) COLLATE utf8_bin,
                                        e_mail VARCHAR (30) COLLATE utf8_bin,
                                        tle VARCHAR (10) COLLATE utf8_bin,
                                        PRIMARY KEY (student_id)) """)
    #ตารางครูผู้สอน
    cs.execute(""" CREATE TABLE teachers (teacher_id INT (3) NOT NULL,
                                        f_name CHAR (30) COLLATE utf8_bin,
                                        l_name CHAR (30) COLLATE utf8_bin,
                                        e_mail VARCHAR (30) COLLATE utf8_bin,
                                        tle VARCHAR (10) COLLATE utf8_bin,
                                        PRIMARY KEY (teacher_id)) """)
    #ตารางรายวิชา
    cs.execute(""" CREATE TABLE subjects (subject_id INT (3) NOT NULL,
                                        subject_name CHAR (30) COLLATE utf8_bin,
                                        unit INT (1),
                                        teacher_id INT (3),
                                        PRIMARY KEY (subject_id)) """)
    #ตารางการลงทะเบียนเรียน
    cs.execute(""" CREATE TABLE registers (student_id INT (5) NOT NULL,
                                        subject_id INT (3) NOT NULL,
                                        semester INT (1) NOT NULL,
                                        register_data DATE,
                                        PRIMARY KEY (student_id, subject_id, semester)) """)
except pymysql.err.OperationalError:
    print("ไม่สามารถเชื่อมต่อฐานข้อมูลได้")
except pymysql.err.ProgrammingError:
    print("คำสั่ง SQL ไม่ถูกต้อง !!")
else:
    print("สร้างฐานข้อมูลสำเร็จ")
con.close()
cs.close()