from tkinter import *
import math as mathematics

Division = Tk()
Division.title("Division")

display=Entry(Division)

global nums, count
count = 0
nums = []

def onClick(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(number))

def divide():
    global nums, count
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
        try:
            display.insert(0, float(nums[0] / ((mathematics.prod(nums[1:])) * second_number)))
        except ZeroDivisionError:
            display.insert(0, "Mathematical Error")
        finally:
            nums=[]
    else:
        display.insert(0, float(second_number))

btn7=Button(Division, text="7", padx=20, pady=10, command=lambda: onClick(7))
btn8=Button(Division, text="8", padx=20, pady=10, command=lambda: onClick(8))
btn9=Button(Division, text="9", padx=20, pady=10, command=lambda: onClick(9))
btn4=Button(Division, text="4", padx=20, pady=10, command=lambda: onClick(4))
btn5=Button(Division, text="5", padx=20, pady=10, command=lambda: onClick(5))
btn6=Button(Division, text="6", padx=20, pady=10, command=lambda: onClick(6))
btn1=Button(Division, text="1", padx=20, pady=10, command=lambda: onClick(1))
btn2=Button(Division, text="2", padx=20, pady=10, command=lambda: onClick(2))
btn3=Button(Division, text="3", padx=20, pady=10, command=lambda: onClick(3))
btn0=Button(Division, text="0", padx=20, pady=10, command=lambda: onClick(0))
btndec=Button(Division, text=".", padx=22, pady=10, command=lambda: onClick("."))
btneq=Button(Division, text="=", padx=18, pady=10, command=equals)
btndiv=Button(Division, text="/", padx=22, pady=10, command=divide)
btnclr=Button(Division, text="CLR", padx=40, pady=10, command=clear)


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
btndiv.grid(row="5", column="0")
btnclr.grid(row="5", column="1", columnspan="2")


Division.mainloop()