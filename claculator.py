from tkinter import*


window = Tk()

window.title("calculator Program")
window.geometry("350x400")

keep_text = " "
label_text = StringVar()

label = Label(window,textvariable=label_text,
              font=("consolas",20),bg="#b6d4b9",width=20, height=2)
label.pack()


window.mainloop()