from tkinter import *

class Vector:

    def __init__(self,n):
        self.top=Tk()
        self.n=n
        self.lst=[]
        self._make_widgets()
        
    def _make_widgets(self):
        
        for i in range(self.n):
            linputV=Label(self.top,
                  text=f"Input component {i}:")
            linputV.pack()
            inpV=Entry(self.top)
            inpV.pack()
            self.lst.append(inpV)

class MainGUI:

    def __init__(self):
        self.top=Tk()
        self._make_widgets()

    def _make_widgets(self):
        def create():
            assert inpN.get(), "an entry is empty"
            global a,b
            a=Vector(int(inpN.get()))
            b=Vector(int(inpN.get()))
            return a,b

        def calc():
            s=0
            lboxA.delete(0,END)
            lboxB.delete(0,END)
            for i,j in enumerate(a.lst):
                assert j.get() and b.lst[i].get(), "an entry is empty"
                s+=float(j.get())*float(b.lst[i].get())
                lboxA.insert(END,j.get())
                lboxB.insert(END,b.lst[i].get())
            lrez.config(text=f"Result: {s}")
            
            return s
        linputN=Label(self.top,
                      text="Input n:")
        linputN.pack()
        inpN=Entry(self.top)
        inpN.pack()
        
        bcreate=Button(self.top, text="Create vectors",
                       command=create)
        bcreate.pack()

        bcalc=Button(self.top, text="Calculate scalar product",
                       command=calc)
        bcalc.pack()

        lrez=Label(self.top,
           text="Result: __",
           fg="cyan", bg="navy")
        lrez.pack()

        lboxA=Listbox(self.top)
        lboxA.pack()

        lboxB=Listbox(self.top)
        lboxB.pack()
if __name__=="__main__":
    a=MainGUI()
    mainloop()
