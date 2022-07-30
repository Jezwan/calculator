from tkinter import *

Subtraction = Tk()
Subtraction.title("Subtraction")

display=Entry(Subtraction)

global nums, count
count = 0
nums = []

def onClick(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(number))

def subtract():
    global count, nums
    count = 0
    nums.append(float(display.get()))
    display.delete(0, END)

def clear():
    display.delete(0, END)

def equals():
    global count, nums
    second_number = float(display.get())
    display.delete(0, END)
    count+=1
    if count == 1:
        display.insert(0, float(nums[0] - (sum(nums[1:])) - second_number))
        nums = []
    else:
        display.insert(0, float(second_number))

btn7=Button(Subtraction, text="7", padx=20, pady=10, command=lambda: onClick(7))
btn8=Button(Subtraction, text="8", padx=20, pady=10, command=lambda: onClick(8))
btn9=Button(Subtraction, text="9", padx=20, pady=10, command=lambda: onClick(9))
btn4=Button(Subtraction, text="4", padx=20, pady=10, command=lambda: onClick(4))
btn5=Button(Subtraction, text="5", padx=20, pady=10, command=lambda: onClick(5))
btn6=Button(Subtraction, text="6", padx=20, pady=10, command=lambda: onClick(6))
btn1=Button(Subtraction, text="1", padx=20, pady=10, command=lambda: onClick(1))
btn2=Button(Subtraction, text="2", padx=20, pady=10, command=lambda: onClick(2))
btn3=Button(Subtraction, text="3", padx=20, pady=10, command=lambda: onClick(3))
btn0=Button(Subtraction, text="0", padx=20, pady=10, command=lambda: onClick(0))
btndec=Button(Subtraction, text=".", padx=22, pady=10, command=lambda: onClick("."))
btneq=Button(Subtraction, text="=", padx=18, pady=10, command=equals)
btnsub=Button(Subtraction, text="-", padx=21, pady=10, command=subtract)
btnclr=Button(Subtraction, text="CLR", padx=40, pady=10, command=clear)


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
btnsub.grid(row="5", column="0")
btnclr.grid(row="5", column="1", columnspan="2")


Subtraction.mainloop()