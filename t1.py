from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Test 1 GUI")
window.geometry('1024x600')

firstLabel = Label(window, text="Choose the Row and Column you'd like to edit.")
firstLabel.grid(columnspan=2, row=0)
firstEntry = Entry(window, width=10)
firstEntry.grid(column=0, row=2)

comboRow = Combobox(window)
comboCol = Combobox(window)
comboRow['values'] = ("Row", 1, 2, 3, 4, 5, 6, 7, 8)
comboRow.current(0)
comboRow.grid(column=0, row=1, sticky=W)
comboCol['values'] = ("Column", 1, 2, 3, 4, 5, 6)
comboCol.current(0)
comboCol.grid(column=1, row=1, sticky=W)

chartFrame = Frame(window, width=500, height=500, relief=GROOVE)
chartFrame.place(x=474, y=50)

standard = [[5, 10, 15, 20, 25, 30],
[35, 40, 45, 50, 55, 60],
[65, 70, 75, 80, 85, 90],
[95, 100, 105, 110, 115, 120],
[125, 130, 135, 140, 145, 150],
[155, 160, 165, 170, 175, 180],
[185, 190, 195, 200, 205, 210],
[215, 220, 225, 230, 235, 240]]

labelList = []
chartxInc = 514
chartyInc = 80
inc = 0

for a in range(8):
    for b in range(6):
        labelList.append(Label(chartFrame, text=(standard[a][b])))
        labelList[inc].grid(column=b, row=a, padx=30, pady=20)
        inc = inc + 1

def clicked():
    row = comboRow.get()
    col = comboCol.get()
    row = int(row)
    col = int(col)
    labelList[(col-1) + ((row-1)*6)].configure(text="update")


updateValue = Button(window, text="Enter Value", command=clicked)
updateValue.grid(column=1, row=2)

window.mainloop()