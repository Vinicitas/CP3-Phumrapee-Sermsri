from tkinter import*
import math

def leftclickbutton(event):
    x = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    labelResult.configure(text = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if x >= 30:
        labelShowInterpret.configure(text = "อ้วนมาก")
    if 25 <= x < 30:
        labelShowInterpret.configure(text = "อ้วน")
    if 23 <= x < 25:
        labelShowInterpret.configure(text = "น้ำหนักเกิน")
    if 18.6 <= x < 23:
        labelShowInterpret.configure(text = "น้ำหนักปกติ เหมาะสม")
    if x <= 18.6:
        labelShowInterpret.configure(text = "ผอมเกินไป")

mainWindow = Tk()
labelHeight = Label(mainWindow,text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindow,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)
calculatebutton = Button(mainWindow,text="คำนวน")
calculatebutton.bind('<Button-1>',leftclickbutton)
calculatebutton.grid(row=2)
labelResult = Label(mainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
labelInterpret = Label(mainWindow,text="แปลผล",bg="green")
labelInterpret.grid(row=3,column=0)
labelShowInterpret = Label(mainWindow,text="ผล")
labelShowInterpret.grid(row=3,column=1)
mainWindow.mainloop()