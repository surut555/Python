for i in range(1,11):
    n = int(input("กรุณาป้อนตัวเลข 1 - 10:"))
    if n >= 11:
        print("คุณป้อนตัวเลขไม่ถูกต้อง !!")
        break
    if n <=10:
        j = n * i
        print("ผลคูณของ %d x %x"%(i, n),j)
print("สิ้นสุดการทำงานของโปรแกรม")