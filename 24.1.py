from tkinter import *

def taylor():
    x=float(inpX.get())
    eps=float(inpEps.get())

    if abs(x)>=1:
        return
    if eps<=0:
        return
    y=1
    t=1
    i=1
    while abs(t)>eps:
        i+=1
        t*=-x*i/(i-1)
        y+=t

        result='expression= {}'.format(y)
        lrez.configure(text=result)
    return y
top=Tk()

linputX=Label(top,
              text="Input x:")
linputX.pack()
inpX=Entry(top)
inpX.pack()

linputEps=Label(top,
                text="input eps:")
linputEps.pack()
inpEps=Entry(top)
inpEps.pack()

lrez=Label(top,
           text="Result: __",
           fg="cyan", bg="navy")
lrez.pack()

bcalc=Button(top, text="Run",
             command=taylor)
bcalc.pack()

bquit=Button(top,text="exit",
             command=top.quit)
bquit.pack()

top.mainloop()
