import csv
try:
    with open(r"/Users/suratsetthanan/Documents/python/08/fine.csv","w+", newline="") as fine:
        csvfine = csv.writer(fine)
        csvfine.writerow(["Apple","Mango","Watermelon"])
        csvfine.writerow(["Banana","Lime","Orange"])
except (FileExistsError, FileNotFoundError):
    print("ไฟล์ถูกสร้างแล้ว หรือ ไม่พบตำแหน่ที่ระบุ")
else:
    print("เขียนไฟล์สำเร็จ")