from tkinter import *

Addition = Tk()
Addition.title("Addition")

display=Entry(Addition)

global added
added = 0

def onClick(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(number))

def add():
    global added
    added += float(display.get())
    display.delete(0, END)

def clear():
    display.delete(0, END)

def equals():
    global added
    second_number = float(display.get())
    display.delete(0, END)
    display.insert(0, float(added + second_number))
    added = 0


btn7=Button(Addition, text="7", padx=20, pady=10, command=lambda: onClick(7))
btn8=Button(Addition, text="8", padx=20, pady=10, command=lambda: onClick(8))
btn9=Button(Addition, text="9", padx=20, pady=10, command=lambda: onClick(9))
btn4=Button(Addition, text="4", padx=20, pady=10, command=lambda: onClick(4))
btn5=Button(Addition, text="5", padx=20, pady=10, command=lambda: onClick(5))
btn6=Button(Addition, text="6", padx=20, pady=10, command=lambda: onClick(6))
btn1=Button(Addition, text="1", padx=20, pady=10, command=lambda: onClick(1))
btn2=Button(Addition, text="2", padx=20, pady=10, command=lambda: onClick(2))
btn3=Button(Addition, text="3", padx=20, pady=10, command=lambda: onClick(3))
btn0=Button(Addition, text="0", padx=20, pady=10, command=lambda: onClick(0))
btndec=Button(Addition, text=".", padx=22, pady=10, command=lambda: onClick("."))
btneq=Button(Addition, text="=", padx=18, pady=10, command=equals)
btnadd=Button(Addition, text="+", padx=20, pady=10, command=add)
btnclr=Button(Addition, text="CLR", padx=40, pady=10, command=clear)


display.grid(row="0", column="0", columnspan="3", pady=20)
btn7.grid(row="1", column="0")
btn8.grid(row="1", column="1")
btn9.grid(row="1", column="2")
btn4.grid(row="2", column="0")
btn5.grid(row="2", column="1")
btn6.grid(row="2", column="2")
btn1.grid(row="3", column="0")
btn2.grid(row="3", column="1")
btn3.grid(row="3", column="2")
btn0.grid(row="4", column="0")
btndec.grid(row="4", column="1")
btneq.grid(row="4", column="2")
btnadd.grid(row="5", column="0")
btnclr.grid(row="5", column="1", columnspan="2")


Addition.mainloop()