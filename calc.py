from tkinter import *
import math as mathematics


window = Tk()
window.title("Calculator")

def buttonAddition():
    
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

def buttonSubtraction():

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

def buttonMultiplication():

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


def buttonDivision():
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


button_Addition = Button(window, text="ADDITION", padx=40, pady=20, command=buttonAddition).grid()
button_Subtraction = Button(window, text="SUBTRACTION", padx=25, pady=20, command=buttonSubtraction).grid()
button_Multiplication = Button(window, text="MULTIPLICATION", padx=16, pady=20, command=buttonMultiplication).grid()
button_Division = Button(window, text="DIVISION", padx=42, pady=20, command=buttonDivision).grid()

window.mainloop()