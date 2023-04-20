from tkinter import *
def button_press(num):
  global keep_text 
  keep_text = keep_text + str(num) 
  label_text.set(keep_text) #กำหนดให้ตัวเลขอยู่ในช่องหน้าจอเครื่องคิดเลข สร้างลำดับที่ 1

def equals(): #ฟังก์ชันนี้สร้างลำดับที่ 2
   global keep_text 
   total = str(eval(keep_text)) 
   label_text.set(total)
   keep_text = total 

def clear():
   global keep_text
   label_text.set(" ")
   keep_text = " "
   

window = Tk()

window.title("calculator Program")
window.geometry("350x400")

keep_text = "" 

label_text = StringVar() 

label = Label(window,textvariable=label_text,
font=("consolas",20),bg="#b6d4b9",width=20, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,text=1,height=2, width=5,font=35,
                 command=lambda:button_press(1))
button1.grid(row = 0, column = 0)

button2 = Button(frame,text=2,height=2, width=5,font=35,
                 command=lambda:button_press(2))
button2.grid(row = 0, column = 1)

button3 = Button(frame,text=3,height=2, width=5,font=35,
                 command=lambda:button_press(3))
button3.grid(row = 0, column = 2)

button4 = Button(frame,text=4,height=2, width=5,font=35,
                 command=lambda:button_press(4))
button4.grid(row = 1, column = 0)

button5 = Button(frame,text=5,height=2, width=5,font=35,
                 command=lambda:button_press(5))
button5.grid(row = 1, column = 1)

button6 = Button(frame,text=6,height=2, width=5,font=35,
                 command=lambda:button_press(6))
button6.grid(row = 1, column = 2)

button7 = Button(frame,text=7,height=2, width=5,font=35,
                 command=lambda:button_press(7))
button7.grid(row = 2, column = 0)

button8 = Button(frame,text=8,height=2, width=5,font=35,
                 command=lambda:button_press(8))
button8.grid(row = 2, column = 1)

button9 = Button(frame,text=9,height=2, width=5,font=35,
                 command=lambda:button_press(9))
button9.grid(row = 2, column = 2)

plus = Button(frame,text="+",height=2, width=5,font=35,
                 command=lambda:button_press("+"))
plus.grid(row = 0, column = 3)

minus = Button(frame,text="-",height=2, width=5,font=35,
                 command=lambda:button_press("-"))
minus.grid(row = 1, column = 3)

multiply = Button(frame,text="*",height=2, width=5,font=35,
                 command=lambda:button_press("*"))
multiply.grid(row = 2, column = 3)

divide = Button(frame,text="/",height=2, width=5,font=35,
                 command=lambda:button_press("/"))
divide.grid(row = 3, column = 3)

button0 = Button(frame,text=0,height=2, width=5,font=35,
                 command=lambda:button_press(0))
button0.grid(row = 3, column = 0)

decimal = Button(frame,text=".",height=2, width=5,font=35,
                 command=lambda:button_press("."))
decimal.grid(row = 3, column = 1)

equal = Button(frame,text="=",height=2, width=5,font=35,
                 command=equals)
equal.grid(row = 3, column = 2)

clear = Button(window,text="clear",height=2, width=5,font=35,
                 command= clear)
clear.pack()

window.mainloop()