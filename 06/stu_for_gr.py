stu = int(input("ป้อนจำนวนนักเรียน"))
for i in range(1, stu +1):
    j = 1
    list=[]
    print("นักเรียนึนที่",i)
    while j <= 5:
        n = float(input("กรอกคะแนนครั้งที่ %d ="%j))
        list.append(n)
        j += 1
    if sum(list) <= 49:
        print("นักเรียนคนที่ %d ได้คะแนน =" %i, list, "คะแนนรวม =",
              sum(list), "เกรด = 0")
    elif sum(list) <= 50:
        print("นักเรียนคนที่ %d ได้คะแนน =" %i, list, "คะแนนรวม =",
              sum(list), "เกรด = 1")
    elif sum(list) <= 55:
        print("นักเรียนคนที่ %d ได้คะแนน =" %i, list, "คะแนนรวม =",
              sum(list), "เกรด = 1.5")
    elif sum(list) <= 60:
        print("นักเรียนคนที่ %d ได้คะแนน =" %i, list, "คะแนนรวม =",
              sum(list), "เกรด = 2")
    elif sum(list) <= 65:
        print("นักเรียนคนที่ %d ได้คะแนน =" %i, list, "คะแนนรวม =",
              sum(list), "เกรด = 2.5")
    elif sum(list) <= 70:
        print("นักเรียนคนที่ %d ได้คะแนน =" %i, list, "คะแนนรวม =",
              sum(list), "เกรด = 3")
    elif sum(list) <= 75:
        print("นักเรียนคนที่ %d ได้คะแนน =" %i, list, "คะแนนรวม =",
              sum(list), "เกรด = 3.5")
    else: 
        print("นักเรียนคนที่ %d ได้คะแนน =" %i, list, "คะแนนรวม =",
              sum(list), "เกรด = 4")
