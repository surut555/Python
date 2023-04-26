import csv
try:
    with open(r"/Users/suratsetthanan/Documents/python/08/Program.csv","w+", newline="") as csvfile:
        program = csv.writer(csvfile, delimiter="\t")
        program.writerow(["Java", "C", "C#"])
        program.writerow(["HTML", "PHP", "GO"])
        program.writerow(["PYTHON", "R", ".NET"])
except FileNotFoundError:
    print("ตำแหน่งบันไพล์ไม่ถูกต้อง")
else:
    print("บันไฟล์สำเร็จ")