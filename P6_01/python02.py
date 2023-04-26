"""age = int(input("กรุณาป้อนอายุของคุณ "))
if age > 35: #รอรับค่าการป้อนข้อมูลเป็นจำนวนเต็ม
    print("อายุของคุณคือ ",age , "ปี")#ตรวจสอบค่าตัวแปร age มากกว่า 35 หรือไม่
if age < 35:
    print("อายุของคุณยังไม่ผ่านเหลือเวลาอีก",35 - age, "ปี")
else:
    print("อายุของคุณผ่านเกณฑ์")"""

f = int(input("Enter first Score : "))
s = int(input("Enter second Score : "))
t = int(input("Enter third Score : "))

total = f + s + t
if total < 49:
    Grade = "F"
elif total < 59:
    Grade = "D"
elif total < 69:
    Grade = "C"
elif total < 70:
    Grade = "B"
else:
    Grade = "A"
print(f"first scord = {f},\n\
        second scord = {s},\n\
        third scord = {t},\n\
        total scord = {total},\n\
        grade = {Grade} ")

