from tkinter import *

class MainGUI:
    def __init__(self,fname):
        self.top=Tk()
        self._make_widgets()
        self.fname=fname
        
    def _make_widgets(self):
        def append():
            a=AppendGUI(self.fname)

        def edit():
            e=EditGUI(self.fname)

        def search():
            s=SearchGUI(self.fname)  
        bAppend=Button(self.top,
                      text="Додати інформацію про знайомого",
                       command=append)
        bAppend.pack()

        bEdit=Button(self.top,
                      text="Редагувати інформацію про знайомого",
                     command=edit)
        bEdit.pack()

        bSearch=Button(self.top,
                      text="Знайти номер телефону",
                       command=search)
        bSearch.pack()

class AppendGUI:
    def __init__(self,fname):
        self.top=Tk()
        self._make_widgets()
        self.fname=fname
        
    def _make_widgets(self):
        def append2():
            f=open(self.fname,"a")
            
            string=string=inpLastName.get()+", "+inpNumber.get()+"\n"
            
            f.write(string)
            f.close()
            self.top.destroy()
        lLastName=Label(self.top,
                      text="Прізвище:")
        lLastName.pack()
        inpLastName=Entry(self.top)
        inpLastName.pack()
        
        lNumber=Label(self.top,
                      text="номер телефону:")
        lNumber.pack()
        inpNumber=Entry(self.top)
        inpNumber.pack()

        bAppend2=Button(self.top,
                        text="Додати",
                        command=append2)
        bAppend2.pack()

class EditGUI:
    def __init__(self,fname):
        self.top=Tk()
        self._make_widgets()
        self.fname=fname
    def _make_widgets(self):
        def edit2():
            f=open(self.fname, "r")
            lines=f.read()
            lines=lines.split("\n")
            new_lines=[]
            for line in lines:
                line=line.split(", ")
                new_lines.append(line)
            f.close()

            string=inpLastName.get()+", "+inpNumber.get()
            
            for i,line in enumerate(new_lines):
                if line[0]==inpLastName.get():
                    lines[i]=string

            new_string=""
            
            for line in lines:
                if line:
                    new_string+=line+"\n"
            f=open(self.fname, "w")
            f.write(new_string)
            f.close()

            self.top.destroy()
            
        lLastName=Label(self.top,
                      text="Прізвище:")
        lLastName.pack()
        inpLastName=Entry(self.top)
        inpLastName.pack()

        lNumber=Label(self.top,
                      text="номер телефону:")
        lNumber.pack()
        inpNumber=Entry(self.top)
        inpNumber.pack()

        bEdit2=Button(self.top,
                        text="Редагувати",
                        command=edit2)
        bEdit2.pack()

class SearchGUI:
    def __init__(self,fname):
        self.top=Tk()
        self._make_widgets()
        self.fname=fname

    def _make_widgets(self):
        def search2():
            f=open(self.fname, "r")
            lines=f.read()
            lines=lines.split("\n")
            
            for line in lines:
                line=line.split(", ")
                if line[0]==inpLastName.get():
                    res=line[1]
                    break
                
            lNumber.config(text=f"Номер: {res}")
            f.close()
            
        lLastName=Label(self.top,
                      text="Прізвище:")
        lLastName.pack()
        inpLastName=Entry(self.top)
        inpLastName.pack()

        bSearch2=Button(self.top,
                        text="Знайти:",
                        command=search2)
        bSearch2.pack()

        lNumber=Label(self.top,
           text="Номер: __",
           fg="cyan", bg="navy")
        lNumber.pack()
if __name__=="__main__":
    a=MainGUI("file2417.txt")
    mainloop()
