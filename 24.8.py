from tkinter import *

class Vector:

    def __init__(self,n):
        self.top=Tk()
        self.n=n
        self._make_widgets()
    def _make_widgets(self):
        def calc():
            listbox.delete(0,END)
            s=0
            for i in lst:
                assert i.get(), "an entry is empty"
                listbox.insert(END,i.get())
                if float(inpA.get())<=float(i.get())<=float(inpB.get()):
                    s+=1
            lrez.configure(text=f"Result: {s}")
            
        lst=[]
        for i in range(self.n):
            linputV=Label(self.top,
                  text=f"Input component {i}:")
            linputV.pack()
            inpV=Entry(self.top)
            inpV.pack()
            lst.append(inpV)

        bcalc=Button(self.top,text="calc",command=calc)
        bcalc.pack()

class Main:
    def __init__(self):
        self.t=Tk()
        self._make_widgets()
        
    def _make_widgets(self):
        def create():
            assert inpN.get() and inpA.get() and inpB.get(), "an entry is empty"
            assert int(inpN.get())>0, "n has to be >0 and an integer"
            return Vector(int(inpN.get()))
        linputN=Label(self.t,
                      text="Input n:")
        linputN.pack()
        global inpN
        inpN=Entry(self.t)
        inpN.pack()

        linputA=Label(self.t,
                      text="Input a:")
        linputA.pack()
        global inpA
        inpA=Entry(self.t)
        inpA.pack()
        
        linputB=Label(self.t,
                      text="Input b:")
        linputB.pack()
        global inpB
        inpB=Entry(self.t)
        inpB.pack()

        bcreate=Button(self.t, text="Create vector",
                       command=create)
        bcreate.pack()

        global lrez
        lrez=Label(self.t,
           text="Result: __",
           fg="cyan", bg="navy")
        lrez.pack()
        
        global listbox
        listbox=Listbox(self.t)
        listbox.pack()
if __name__=="__main__":
    a=Main()
    mainloop()
