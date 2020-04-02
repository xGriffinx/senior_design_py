from tkinter import *
from tkinter.ttk import *
import functools as fn

window = Tk()
window.title("Test 1 GUI")
window.geometry('1024x600')

chartFrame = Frame(window, width=500, height=500, relief=GROOVE)
chartFrame.place(x=100, y=25)

standard = ['Fill', 10, 15, 20, 25, 30,
35, 40, 45, 50, 55, 60,
65, 70, 75, 80, 85, 90,
95, 100, 105, 110, 115, 120,
125, 130, 135, 140, 145, 150,
155, 160, 165, 170, 175, 180,
185, 190, 195, 200, 205, 210,
215, 220, 225, 230, 235, 240]

labelList = []
chartxInc = 514
chartyInc = 80
inc = 0

def popup(inc):
    popup = Tk()
    popup.title("Update Value")

    label = Label(popup, text="Choose the new value")
    label.grid(columnspan=2, row=0, padx=20, pady=20, sticky=NSEW)

    updateCombo = Combobox(popup, width=15, values=standard)
    updateCombo.current(inc)
    updateCombo.grid(column=0, row=1, padx=20, pady=20, sticky=NSEW)

    def update(inc):
        labelList[inc]["text"] = updateCombo.get()

    updateButton = Button(popup, text="Update", command=fn.partial(update, inc))
    updateButton.grid(row=2, padx=20, pady=10, sticky=NSEW)

    closeButton = Button(popup, text="Close", command=popup.destroy)
    closeButton.grid(row=3, padx=20, pady=10, sticky=NSEW)

    popup.mainloop()

for a in range(8):
    for b in range(6):
        labelList.append(Button(chartFrame, text=standard[inc], command=fn.partial(popup, inc)))
        labelList[inc].grid(column=b, row=a, padx=30, pady=20)
        inc = inc + 1

def startProg():
    print("Starting Program lel")
    for i in labelList:
        print(i["text"])

def endProg():
    print("Ending Program lelel")

Style().configure('greenStart.TButton', background='spring green')
Style().configure('redEnd.TButton', background='red')

startBut = Button(window, text="Start", style='greenStart.TButton', command=startProg)
startBut.place(x=400, y=560)

endBut = Button(window, text="End", style='redEnd.TButton', command=endProg)
endBut.place(x=538, y=560)

window.mainloop()