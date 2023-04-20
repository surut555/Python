sut = int(input("ป้อนจำนวนนักเรียน ="))
for i in range(1, sut + 1):
    j = 1
    list = []
    print("นักเรียนที่",i)
    while j <= 5:
        n = float(input("กรุณาป้อนคะแนนครั้งที่ %d =" %j))
        list.append(n)
        j += 1
    print("นักเรียนคนที่ %d ได้คะแนน =" %i, list, "คะแนนรวม =",
          sum(list))