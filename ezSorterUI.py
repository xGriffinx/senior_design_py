from tkinter import *
from tkinter.ttk import *
import functools as fn

window = Tk()
window.title("EZ Resistor Sorter")
window.geometry('1024x600')

tab_Parent = Notebook(window)

tab1 = Frame(tab_Parent)
tab2 = Frame(tab_Parent)

tab_Parent.add(tab1, text="Home")
tab_Parent.add(tab2, text="Update Values")

tab_Parent.pack(expand=1, fill='both')

defaultValues = [10, 12, 15, 22, 33, 47, 56, 68, 82, 100, 
120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 
820, 1000, 1200, 1500, 1800, 2200, 2700, 3300, 3900, 
4700, 5600, 6800, 8200, 10000, 12000, 15000, 18000, 22000, 
27000, 33000, 39000, 47000, 56000, 68000, 82000, 100000, 
120000, 150000, 180000, 220000, 270000, 330000, 390000, 430000, 
470000, 560000, 680000, 820000, 1000000, 4700000] 

standardValues = ['Empty', 1, 2, 3, 10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 
27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91, 100, 110, 
120, 130, 150, 160, 180, 200, 220, 240, 270, 300, 330, 360, 390, 
430, 470, 510, 560, 620, 680, 750, 820, 910, 1000, 1100, 1200, 
1300,1500,1600,1800,2000,2200,2400,2700,3000,3300,3600,3900,
4300,4700,5100,5600,6200,6800,7500,8200,9100,100000,110000,
120000,130000,150000,160000,180000,200000,220000,240000,
270000,300000,330000,360000,390000,430000,470000,510000,
560000,620000,680000,750000,820000,910000,1000000,1500000,
2000000,3000000,4700000,5600000,7500000,9100000]

#### Resistor Color Band Styles ####
Style().configure('default-resistorBand.TLabel', background = 'gray', foreground = 'gray', relief=RAISED) #Default - Gray
Style().configure('black-rB.TLabel', background='black', foreground='black', relief=RAISED) #Black 0, 1ohm
Style().configure('brown-rB.TLabel', background='saddle brown', foreground='saddle brown', relief=RAISED) #Brown 1, 10ohm
Style().configure('red-rB.TLabel', background = 'red', foreground='red', relief=RAISED) #Red 2, 100ohm
Style().configure('orange-rB.TLabel', background = 'dark orange', foreground='dark orange', relief=RAISED) #Orange 3, 1kohm
Style().configure('yellow-rB.TLabel', background = 'yellow', foreground='yellow', relief=RAISED) #Yellow 4, 10kohm
Style().configure('green-rB.TLabel', background = 'green', foreground='green', relief=RAISED) #Green 5, 100kohm
Style().configure('blue-rB.TLabel', background = 'blue', foreground='blue', relief=RAISED) #Blue 6, 1Mohm
#Violet 7, 10Mohm
#Gray 8, 100Mohm
#White 9, 1Gohm

Style().configure('gold-rB.TLabel', background = 'goldenrod', foreground='goldenrod', relief=RAISED)
Style().configure('silver-rB.TLabel', background = 'snow3', foreground='snow3', relief=RAISED)

#### TAB 1 ####

readoutFrame = Frame(tab1, width = 100, height=100)
readoutFrame.place(x=400, y=200)

currentStatus = Label(readoutFrame, text="Status:")
currentStatus.grid(row=0, column=0, sticky=E)

currentStatus_Value = Label(readoutFrame, text="Stopped")
currentStatus_Value.grid(row=0, column=1)

readoutLabel_Text = Label(readoutFrame, text="Last Measured Resistor:")
readoutLabel_Text.grid(row=1, column=0, sticky=E)

readoutLabel_Value = Label(readoutFrame, text="")
readoutLabel_Value.grid(row=1, column=1)

resistorFrame = Frame(tab1, width=600, height=100, relief=GROOVE)
resistorFrame.place(x=175, y=250)

resistorBand1 = Label(resistorFrame, width=25, style = 'default-resistorBand.TLabel')
resistorBand1.grid(row=0, column = 0, padx = 10, pady=15)

resistorBand2 = Label(resistorFrame, width=25, style = 'default-resistorBand.TLabel')
resistorBand2.grid(row = 0, column=1, padx = 10, pady=15)

resistorBand3 = Label(resistorFrame, width=25, style = 'default-resistorBand.TLabel')
resistorBand3.grid(row=0, column=2, padx = 10, pady=15)

toleranceBand = Label(resistorFrame, width=25, style = 'default-resistorBand.TLabel')
toleranceBand.grid(row=0, column=3, padx=10, pady=15)

def testcolor100():
    resistorBand1.configure(style='brown-rB.TLabel') #Brown
    resistorBand2.configure(style='black-rB.TLabel') #Black
    resistorBand3.configure(style='brown-rB.TLabel') #Brown
    toleranceBand.configure(style='gold-rB.TLabel') #Tolerance
    readoutLabel_Value["text"] = 100

def testcolor1000():
    resistorBand1.configure(style='brown-rB.TLabel') #Br
    resistorBand2.configure(style='black-rB.TLabel') #Bl
    resistorBand3.configure(style='red-rB.TLabel') #Red
    toleranceBand.configure(style='gold-rB.TLabel') #Tolerance
    readoutLabel_Value["text"] = 1000

def testcolor56K():
    resistorBand1.configure(style='green-rB.TLabel') #Gr
    resistorBand2.configure(style='blue-rB.TLabel') #Blue
    resistorBand3.configure(style='orange-rB.TLabel') #Or
    toleranceBand.configure(style='gold-rB.TLabel') #Tolerance
    readoutLabel_Value["text"] = 56000

def testcolor33M():
    resistorBand1.configure(style='orange-rB.TLabel') #Or
    resistorBand2.configure(style='orange-rB.TLabel') #Or
    resistorBand3.configure(style='green-rB.TLabel') #Gr
    toleranceBand.configure(style='silver-rB.TLabel') #Tolerance
    readoutLabel_Value["text"] = 3300000

testBut100 = Button(tab1, text="Test 100 ohms", width=15, command=testcolor100)
testBut100.place(x=308, y=310)

testBut1000 = Button(tab1, text="Test 1000 ohms", width=15, command=testcolor1000)
testBut1000.place(x=418, y=310)

testBut56K = Button(tab1, text="Test 56 Kohms", width=15, command=testcolor56K)
testBut56K.place(x=528, y=310)

testBut33M = Button(tab1, text="Test 3.3 Mohms", width=15, command=testcolor33M)
testBut33M.place(x=638, y=310)

#### TAB 2 ####

chartFrame = Frame(tab2, width=500, height=500, relief=GROOVE)
chartFrame.place(x=150, y=25)

labelList = []
inc = 0

def popup(inc):
    popup = Tk()
    popup.title("Update Value")

    label = Label(popup, text="Choose the new value")
    label.grid(columnspan=2, row=0, padx=20, pady=20, sticky=NSEW)

    updateCombo = Combobox(popup, width=15, values=standardValues)
    updateCombo.current(0)
    updateCombo.grid(column=0, row=1, padx=20, pady=20, sticky=NSEW)

    def update(inc):
        labelList[inc]["text"] = updateCombo.get()

    updateButton = Button(popup, text="Update", command=fn.partial(update, inc))
    updateButton.grid(row=2, padx=20, pady=10, sticky=NSEW)

    closeButton = Button(popup, text="Close", command=popup.destroy)
    closeButton.grid(row=3, padx=20, pady=10, sticky=NSEW)

    popup.mainloop()

for a in range(10):
    for b in range(6):
        labelList.append(Button(chartFrame, text=defaultValues[inc], command=fn.partial(popup, inc)))
        labelList[inc].grid(column=b, row=a, padx=30, pady=12)
        inc = inc + 1

def startProg():
    print("Starting Program")
    for button in labelList:
        button["state"] = "disabled"
    tab_Parent.select(tab1)
    currentStatus_Value["text"] = "Running"
    startBut["state"] = "disabled"
    endBut["state"] = "enabled"

def endProg():
    print("Ending Program")
    for button in labelList:
        button["state"] = "enabled"
    currentStatus_Value["text"] = "Stopped"
    endBut["state"] = "disabled"
    startBut["state"] = "enabled"

Style().configure('greenStart.TButton', background='spring green')
Style().configure('redEnd.TButton', background='red')

startBut = Button(window, text="Start", style='greenStart.TButton', command=startProg)
startBut.place(x=35, y=50)

endBut = Button(window, text="Stop", style='redEnd.TButton', state="disabled", command=endProg)
endBut.place(x=35, y=90)

window.mainloop()
