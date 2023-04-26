import csv
try:
    file = csv.reader(open(r"/Users/suratsetthanan/Documents/python/08/fine.csv", "r"))
except FileNotFoundError:
    print("ไม่พบไฟล์ที่ระบุ")
else:
    for data in file:
        print("{}, {}, {}".format(data[0], data[1],data[2]))