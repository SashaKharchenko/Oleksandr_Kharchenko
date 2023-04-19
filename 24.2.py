from tkinter import *

def palindrome():
    s=str(inpS.get())

    if s==s[::-1]:
        y="True"
    else:
        y="False"

    result='expression= {}'.format(y)
    lrez.configure(text=result)
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
             command=palindrome)
bcalc.pack()

bquit=Button(top,text="exit",
             command=top.quit)
bquit.pack()

top.mainloop()
