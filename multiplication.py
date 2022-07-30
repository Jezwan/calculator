from tkinter import *

Multiplication = Tk()
Multiplication.title("Multiplication")

display=Entry(Multiplication)

global product
product = 1

def onClick(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(number))

def multiply():
    global product
    product *= float(display.get())
    display.delete(0, END)

def clear():
    display.delete(0, END)

def equals():
    global product
    second_number = float(display.get())
    display.delete(0, END)
    display.insert(0, float(product * second_number))
    product = 1

btn7=Button(Multiplication, text="7", padx=20, pady=10, command=lambda: onClick(7))
btn8=Button(Multiplication, text="8", padx=20, pady=10, command=lambda: onClick(8))
btn9=Button(Multiplication, text="9", padx=20, pady=10, command=lambda: onClick(9))
btn4=Button(Multiplication, text="4", padx=20, pady=10, command=lambda: onClick(4))
btn5=Button(Multiplication, text="5", padx=20, pady=10, command=lambda: onClick(5))
btn6=Button(Multiplication, text="6", padx=20, pady=10, command=lambda: onClick(6))
btn1=Button(Multiplication, text="1", padx=20, pady=10, command=lambda: onClick(1))
btn2=Button(Multiplication, text="2", padx=20, pady=10, command=lambda: onClick(2))
btn3=Button(Multiplication, text="3", padx=20, pady=10, command=lambda: onClick(3))
btn0=Button(Multiplication, text="0", padx=20, pady=10, command=lambda: onClick(0))
btndec=Button(Multiplication, text=".", padx=22, pady=10, command=lambda: onClick("."))
btneq=Button(Multiplication, text="=", padx=18, pady=10, command=equals)
btnmult=Button(Multiplication, text="x", padx=20, pady=10, command=multiply)
btnclr=Button(Multiplication, text="CLR", padx=40, pady=10, command=clear)


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
btnmult.grid(row="5", column="0")
btnclr.grid(row="5", column="1", columnspan="2")


Multiplication.mainloop()
