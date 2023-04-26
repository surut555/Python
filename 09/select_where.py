import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",passwd="",db="register")
    cs = con.cursor()
    cs.execute("SELECT * FROM subjects where teacher_id = 105")
except pymysql.err.OperationalError:
    print("ไม่สามารถติดต่อฐานข้อมูลได้")
except pymysql.err.ProgrammingError:
    print("คุณเขียนคำสั่ง SQL ผิดพลาด")

else:
    print("{:<15}{:<20}{:<10}{}".format("subject_id", "subject_name","unit","teacher_id"))
    data = cs.fetchall()
    for (subject_id, subject_name, unit,teacher_id) in data:
        print("{:<15}{:<20}{:<10}{}".format(subject_id, subject_name,unit,teacher_id))
    con.close()
    cs.close()