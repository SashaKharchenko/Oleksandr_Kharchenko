from tkinter import *

class matrix:
    def __init__(self, n, m, title=""):
        self.top=Tk()
        self.lst=[]
        self.n=n
        self.m=m
        self.title=title
        self._make_widgets()

    def _make_widgets(self):
        linputT=Label(self.top,
                      text=self.title)
        linputT.grid(row=0, column=0, columnspan=self.m)
        r=[]
        for i in range(self.n):
            for j in range(self.m):
                linputM=Label(self.top,
                  text=f"Input element {i}, {j}:")
                linputM.grid(row=2*i+1, column=j)
                inpM=Entry(self.top)
                inpM.grid(row=2*i+2, column=j,padx=5,pady=5)
                r.append(inpM)
            self.lst.append(r)
            r=[]

    def __mul__(self,other):
        assert len(self.lst[0])==len(other.lst), "matrix length mismatch"
        Mmatr=[]
        lst=[]
        a=0
        for i in range(len(self.lst)):
            for j in range(len(other.lst[0])):
                for k in range(len(self.lst[0])):
                    a+=float(self.lst[i][k].get())*float(other.lst[k][j].get())
                lst.append(a)
                a=0
            Mmatr.append(lst)
            lst=[]
        return Mmatr
class MainGUI:
    def __init__(self):
        self.t=Tk()
        self._make_widgets()

    def _make_widgets(self):
        
        def create():
            global a,b
            assert inpN1.get() and inpM1.get() and inpN2.get() and inpM1.get(), "an entry is empty"
            a=matrix(int(inpN1.get()), int(inpM1.get()),"matrix 1")
            b=matrix(int(inpN2.get()), int(inpM2.get()), "matrix 2")
            
        def calc():
            lboxA.delete(0,END)
            lboxB.delete(0,END)
            lboxRez.delete(0,END)
            for i in a.lst:
                string=""
                for j in i:
                    assert j.get(), "an entry is empty"
                    string+=j.get()
                    string+=" "
                lboxA.insert(END,string)
                
            for i in b.lst:
                string=""
                for j in i:
                    assert j.get(), "an entry is empty"
                    string+=j.get()
                    string+=" "
                lboxB.insert(END,string)

            rezMatrix=a*b

            for i in rezMatrix:
                string=""
                for j in i:
                    string+=str(j)
                    string+=" "
                lboxRez.insert(END,string)
        
        linputN1=Label(self.t,
                       text="Input n1:")
        linputN1.grid(row=0, column=0)
        inpN1=Entry(self.t)
        inpN1.grid(row=1, column=0,padx=5,pady=5)

        linputM1=Label(self.t,
                       text="Input m1:")
        linputM1.grid(row=0, column=1)
        inpM1=Entry(self.t)
        inpM1.grid(row=1, column=1,padx=5,pady=5)

        linputN2=Label(self.t,
                       text="Input n2:")
        linputN2.grid(row=2, column=0)
        inpN2=Entry(self.t)
        inpN2.grid(row=3, column=0,padx=5,pady=5)

        linputM2=Label(self.t,
                       text="Input m1:")
        linputM2.grid(row=2, column=1)
        inpM2=Entry(self.t)
        inpM2.grid(row=3, column=1,padx=5,pady=5)

        bcreate=Button(self.t, text="Create matrices",
                       command=create)
        bcreate.grid(row=4, column=0, columnspan=2,pady=5)

        bcalc=Button(self.t, text="Calculate product",
                       command=calc)
        bcalc.grid(row=5, column=0, columnspan=2,pady=5)

        lA=Label(self.t,
                 text="matrix 1")
        lA.grid(row=6, column=0)

        lB=Label(self.t,
                 text="matrix 2")
        lB.grid(row=6, column=1)
        
        lboxA=Listbox(self.t)
        lboxA.grid(row=7,column=0)

        lboxB=Listbox(self.t)
        lboxB.grid(row=7,column=1)

        lrez=Label(self.t,
                   text="result matrix")
        lrez.grid(row=8,column=0,columnspan=2)

        lboxRez=Listbox(self.t)
        lboxRez.grid(row=9, column=0, columnspan=2)
if __name__=="__main__":
    a=MainGUI()
    mainloop()
