#การเขียนคำสั่งโปรแกรมควบคุมทิศทางแบบมีเงื่อนไข
#nested if ตรวจสอบจำนวนเงินที่สามารถซื้อโทรศัพท์
money = int(input("กรุณาป้อนจำนวนเงินของคุณ :"))
if money >= 30000:
    if money >= 50000:
        print("คุณสามารถซื้อโทรศัพท์ iphone 14 Pro")
    else:
        print("คุณสามารถซื้อโทรศัพท์ iphone 14 ")
elif money >= 35000:
    if money >= 25000:
       print("คุณสามารถซื้อโทรศัพท์ iphone 13 ") 
    else:
        print("คุณสามารถซื้อโทรศัพท์ iphone 12 ")
else:
    print("ยอดเงินของคุณไม่เพียงพอต่อการชำระ")