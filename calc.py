from tkinter import *

window = Tk()
window.title("Calculator")

buttonAddition = Button(window, text="ADDITION", padx=40, pady=20).grid()
buttonSubtraction = Button(window, text="SUBTRACTION", padx=25, pady=20).grid()
buttonMultiplication = Button(window, text="MULTIPLICATION", padx=16, pady=20).grid()
buttonDivision = Button(window, text="DIVISION", padx=42, pady=20).grid()

window.mainloop()