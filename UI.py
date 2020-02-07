from tkinter import (Tk, StringVar, Entry, Button, RIGHT)

root = Tk()

class UI:
    
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.standardCalculator()
        self.updateFrame()

    def standardCalculator(self):
        self.listedNumbers = StringVar()
        self.manualEntry = Entry(self.master, textvar=self.listedNumbers, width=35, justify=RIGHT)

        self.sevenButton = Button(self.master, text="7", command=self.sevenButtonPress, height=2, width=10)
        self.eightButton = Button(self.master, text="8", command=self.eightButtonPress, height=2, width=10)
        self.nineButton = Button(self.master, text="9", command=self.nineButtonPress, height=2, width=10)
        self.fourButton = Button(self.master, text="4", command=self.fourButtonPress, height=2, width=10)
        self.fiveButton = Button(self.master, text="5", command=self.fiveButtonPress, height=2, width=10)
        self.sixButton = Button(self.master, text="6", command=self.sixButtonPress, height=2, width=10)
        self.oneButton = Button(self.master, text="1", command=self.oneButtonPress, height=2, width=10)
        self.twoButton = Button(self.master, text="2", command=self.twoButtonPress, height=2, width=10)
        self.threeButton = Button(self.master, text="3", command=self.threeButtonPress, height=2, width=10)
        self.zeroButton = Button(self.master, text="0", command=self.zeroButtonPress, height=2, width=10)
        self.decimalButton = Button(self.master, text=".", command=self.decimal, height=2, width=10)
        self.equalsButton = Button(self.master, text="=", command=self.total, height=2, width=10)

        self.backspaceButton = Button(self.master, text="<", command=self.backspace, height=2, width=10)
        self.divisionButton = Button(self.master, text="/", command=self.divide, height=2, width=10)
        self.multiplicationButton = Button(self.master, text="*", command=self.multiply, height=2, width=10)
        self.subtractionButton = Button(self.master, text="-", command=self.subtract, height=2, width=10)
        self.additionButton = Button(self.master, text="+", command=self.add, height=2, width=10)
        self.clearButton = Button(self.master, text="C", command=self.clear, height=2, width=10)

    def updateFrame(self):
        self.manualEntry.grid(column=0, columnspan=3, row=0, rowspan=2)
        #==========Ten Key Buttons===========#
        self.sevenButton.grid(column=0, row=2)
        self.eightButton.grid(column=1, row=2)
        self.nineButton.grid(column=2, row=2)

        self.fourButton.grid(column=0, row=3)
        self.fiveButton.grid(column=1, row=3)
        self.sixButton.grid(column=2, row=3)

        self.oneButton.grid(column=0, row=4)
        self.twoButton.grid(column=1, row=4)
        self.threeButton.grid(column=2, row=4)

        self.zeroButton.grid(column=0, row=5)
        self.decimalButton.grid(column=1, row=5)
        self.equalsButton.grid(column=2, row=5)
        #==========Operator Buttons===========#
        self.clearButton.grid(column=3, row=0)
        self.backspaceButton.grid(column=3, row=1)
        self.divisionButton.grid(column=3, row=2)
        self.multiplicationButton.grid(column=3, row=3)
        self.subtractionButton.grid(column=3, row=4)
        self.additionButton.grid(column=3, row=5)

    def oneButtonPress(self):
        self.numberEnter(1)

    def twoButtonPress(self):
        self.numberEnter(2)

    def threeButtonPress(self):
        self.numberEnter(3)

    def fourButtonPress(self):
        self.numberEnter(4)

    def fiveButtonPress(self):
        self.numberEnter(5)

    def sixButtonPress(self):
        self.numberEnter(6)

    def sevenButtonPress(self):
        self.numberEnter(7)

    def eightButtonPress(self):
        self.numberEnter(8)

    def nineButtonPress(self):
        self.numberEnter(9)

    def zeroButtonPress(self):
        self.numberEnter(0)

    def numberEnter(self, value):
        var =self.listedNumbers.get()
        self.listedNumbers.set(var + str(value))

    def add(self):
        self.numberEnter("+")

    def subtract(self):
        self.numberEnter("-")
    
    def multiply(self):
        self.numberEnter("*")
    
    def divide(self):
        self.numberEnter("/")

    def decimal(self):
        self.numberEnter(".")

    def backspace(self):
        var = self.listedNumbers.get()
        self.manualEntry.delete(len(var) - 1)

    def total(self):
        var = self.listedNumbers.get()
        rav = eval(var)
        self.listedNumbers.set(rav)
    
    def clear(self):
        self.manualEntry.delete(0, len(self.listedNumbers.get()))

ui= UI(root)
root.mainloop()
