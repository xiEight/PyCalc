from tkinter import*
def add():
    global x
    global y
    try:
        xx = int(x.get())
        yy = int(y.get())
        s = str(xx + yy)
    except ValueError:
        s = "Value must be integers!"
    finally:
        l['text'] = s
        l.pack()

def mins():
    global x
    global y
    try:
        xx = int(x.get())
        yy = int(y.get())
        s = str(xx - yy)
    except ValueError:
        s = "Value must be integers!"
    finally:
        l['text'] = s
        l.pack()

def mult():
    global x
    global y
    try:
        xx = int(x.get())
        yy = int(y.get())
        s = str(xx * yy)
    except ValueError:
        s = "Value must be integers!"
    finally:
        l['text'] = s
        l.pack()

def divz():
    global x
    global y
    global l
    try:
        xx = int(x.get())
        yy = int(y.get())
        s = str(xx / yy)
    except ValueError:
        s = "Value must be integers!"
    except ZeroDivisionError:
        s = "Division by 0!"
    finally:
        l['text'] = s
        l.pack()



   
root = Tk()
x = Entry(justify = "center",width = 30)
y = Entry(justify = "center",width = 30)
pls = Button(text = '+', command = add,width = 30)
mns = Button(text = '-', command = mins,width = 30)
mul = Button(text = '*', command = mult,width = 30)
dv = Button(text = '/', command = divz,width = 30)
x.pack()
y.pack()
dv.pack()
mul.pack()
mns.pack()
pls.pack()
l = Label()
root.mainloop()
