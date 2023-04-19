from tkinter import *

def func():
    s=str(inpS.get())
    lst=list(map(float,s.split()))
    y=0
    for i in range(len(lst)-1):
        if lst[i]*lst[i+1]<0:
            y+=1
    result='{}'.format(y)
    lrez.configure(text=result)
    inpS.delete(0,END)
    return y
top=Tk()

linputS=Label(top,
              text="Input string:")
linputS.pack()
inpS=Entry(top)
inpS.pack()

lrez=Label(top,
           text="Result: __",
           fg="cyan", bg="navy")
lrez.pack()

bcalc=Button(top, text="Run",
             command=func)
bcalc.pack()

bquit=Button(top,text="exit",
             command=top.quit)
bquit.pack()

top.mainloop()
