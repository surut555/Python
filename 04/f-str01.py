#การเขียนคำส่ังโปรแกรมจัดรูปแบบการแสดงผลด้วย f-string
f = int(input("Enter first score:"))
s = int(input("Enter second score:"))
t = int(input("Enter third score:"))

total = f + s + t
if total < 49:
    Grade = "F"
elif total < 59:
    Grade = "D"
elif total < 69:
    Grade = "C"
elif total < 79:
    Grade = "B"
else:
    Grade = "A"
print(f"first score = {f},\n\
      second score = {s},\n\
      third score = {t},\n\
      total score = {total},\n\
      grade = {Grade} " )