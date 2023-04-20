#การเขียนโปรแกรมควบคุมทิศทางแบบมีเงื่อนไข if elif else
sex = input("กรุณาป้อนเพศของคุณ :")
size = int(input("กรุณาป้อนขนาดหน้าอก"))
if sex == "male":
    if size <= 38:
        print("size = s ชาย")
    elif size <= 40:
        print("size = m ชาย")
    elif size <= 42:
        print("size = l ชาย")
    else:
        print("size = xl ชาย")
if sex == "female":
    if size <= 34:
        print("size = s หญิง")
    elif size <= 36:
        print("size = m หญิง")
    elif size <= 38:
        print("size = l หญิง")
    else:
        print("size = xl")