from tkinter import *
import math as mathematics

window = Tk()
window.title("Calculator")
display=Entry(window)

global added, nums, product, count
added = 0
count = 0
nums = []
product = 1

def onClick(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(number))

def add():
    global added, math
    math = "add"
    added += float(display.get())
    display.delete(0, END)
    
def subtract():
    global math, count, nums
    math = "subtract"
    count = 0
    nums.append(float(display.get()))
    display.delete(0, END)

def multiply():
    global math, product
    math = "multiply"
    product *= float(display.get())
    display.delete(0, END)

def divide():
    global math, nums, count
    math = "divide"
    count = 0
    nums.append(float(display.get()))
    display.delete(0, END)

def clear():
    display.delete(0, END)

def equals():
    global added, count, nums, product
    second_number = float(display.get())
    display.delete(0, END)


    if math == "add":
        display.insert(0, float(added + second_number))
        added = 0


    if math == "subtract":
        count+=1
        if count == 1:
            display.insert(0, float(nums[0] - (sum(nums[1:])) - second_number))
            nums = []
        else:
            display.insert(0, float(second_number))
    

    if math == "multiply":
        display.insert(0, float(product * second_number))
        product = 1


    if math == "divide":
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
        

btn7=Button(window, text="7", padx=20, pady=10, command=lambda: onClick(7))
btn8=Button(window, text="8", padx=20, pady=10, command=lambda: onClick(8))
btn9=Button(window, text="9", padx=20, pady=10, command=lambda: onClick(9))
btn4=Button(window, text="4", padx=20, pady=10, command=lambda: onClick(4))
btn5=Button(window, text="5", padx=20, pady=10, command=lambda: onClick(5))
btn6=Button(window, text="6", padx=20, pady=10, command=lambda: onClick(6))
btn1=Button(window, text="1", padx=20, pady=10, command=lambda: onClick(1))
btn2=Button(window, text="2", padx=20, pady=10, command=lambda: onClick(2))
btn3=Button(window, text="3", padx=20, pady=10, command=lambda: onClick(3))
btn0=Button(window, text="0", padx=20, pady=10, command=lambda: onClick(0))
btndec=Button(window, text=".", padx=22, pady=10, command=lambda: onClick("."))
btneq=Button(window, text="=", padx=18, pady=10, command=equals)
btnadd=Button(window, text="+", padx=19, pady=10, command=add)
btnsub=Button(window, text="-", padx=21, pady=10, command=subtract)
btnmult=Button(window, text="x", padx=20, pady=10, command=multiply)
btndiv=Button(window, text="/", padx=22, pady=10, command=divide)
btnclr=Button(window, text="CLR", padx=10, pady=30, command=clear)

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
btnsub.grid(row="5", column="1")
btnmult.grid(row="6", column="0")
btndiv.grid(row="6", column="1")
btnclr.grid(row="5", column="2", rowspan="2")

window.mainloop()