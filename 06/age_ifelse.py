#การเขียนคำสั่งโปรแกรมตรวจสอบเงื่อนไขด้วยคำสั่ง if else ตรวจสอบอายุ
age = int(input("กรุณาป้อนอายุของคุณ ="))
if age > 30:
    print("อายุของคุณคือ ", age ,"ปี")
if age < 30:
    print("อายุของคุณยังไม่ผ่านเหลือเวลาอีก",30 - age,"ปี")
else:
    print("อายุของคุณผ่านเกณฑ์")