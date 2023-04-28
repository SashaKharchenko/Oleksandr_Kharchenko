from tkinter import *

class calculatorGui:

    def __init__(self, forma):

        self.frame=forma
        self.frame.title("Calculator")

        self.eq=Entry(self.frame, width=100)
        self.eq.grid(row=0, column=0, padx=5, pady=5)
        
        self.createButton()

    def createButton(self):

        digits=[i for i in range(10)]
        operations=['+','-','*','/','c','=','^','sqrt']

        full_buttons_list=digits+operations

        n=len(full_buttons_list)

        Buttons=[None for _ in range(n)]

        rows=[[None for _ in range(4)] for __ in range(n//4+1)]
        
        for i,symb in enumerate(full_buttons_list):
            Buttons[i]=self.addButton(symb)
            rows[i//4][i%4]=Buttons[i]
            
        for i,row in enumerate(rows):
            for j,button in enumerate(row):
                button.grid(row=i, column=j+1, columnspan=1)
    def addButton(self, button_name):
        return Button(self.frame, text=button_name, width=10,
                      command=lambda: self.clickButton(str(button_name)))

    def clickButton(self,x):
        equation=self.eq.get()
        
        if x=="c":
            self.eq.delete(0,END)

        elif x == '=':
            answer=(str(eval(equation)))
            self.eq.delete(0,END)
            self.eq.insert(0,answer)

        else:
            self.eq.delete(0,END)
            self.eq.insert(0,equation+x)
        
if __name__=="__main__":

    root=Tk()

    gui_calc=calculatorGui(root)

    root.mainloop()
