from tkinter import *
def inpList():
    s=str(inpS.get())
    lst=s.split()
    for i in lst:
        listbox.insert(END,i)
root=Tk()
root.geometry("200x220")
frame=Frame(root)
frame.pack()

linputS=Label(root,
              text="Input string:")
linputS.pack()
inpS=Entry(root)
inpS.pack()

label=Label(root,text="A list of Grocery items.")
label.pack()

bcalc=Button(root, text="Run",
             command=inpList)
bcalc.pack()

listbox=Listbox(root)
listbox.pack()
root.mainloop()

