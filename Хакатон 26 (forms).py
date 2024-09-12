import tkinter as tk

class FormConstructor:
    def __init__(self, master, form_file):
        self.master=master
        self.form_file=form_file
        self.fields=[]
        self.entries=[]
        self.current_row=0
        self.master.title('Form Constructor')
        self.master.geometry('400x300')

        with open(self.form_file, 'r') as f:
            for line in f:
                name, field=line.split(' ', 1)[0], line.split(' ', 1)[1][:-1]
                if field.startswith('{'):

                    field_type=field.strip('{}')
                    label=tk.Label(self.master, text=name)
                    label.grid(row=self.current_row, column=0)
                    entry=tk.Entry(self.master)
                    entry.grid(row=self.current_row, column=1)
                    self.fields.append((name, field_type))
                    self.entries.append(entry)
                elif field.startswith("["):
                    options=[option.strip() for option in field.strip('[]').split(",")]
                    options=[option.strip("'") for option in options]
                    label=tk.Label(self.master, text=name)
                    label.grid(row=self.current_row, column=1)
                    self.fields.append((name,options))
                    self.entries.append(var)
                self.current_row+=1

        def save_data(self,output):
            data=[]
            for entry in self.entries:
                if isinstance(entry, tk.StringVar):
                    data.append(entry.get())
                elif isinstance(entry, tk.Entry):
                    data.append(entry.get())
            with open(output, 'a') as f:
                f.write(','.join(['"{}"'.format(d) for d in data])+"\n")
            for entry in self.entries:
                if isinstance(entry, tk.StringVar):
                    entry.set(entry.get().split(',')[0])
                elif isinstance(entry, tk.Entry):
                    entry.delete(0, tk.END)

        def clear_form(self):
            for entry in self.entries:
                if isinstance(entry, tk.StringVar):
                    entry.set(entry.get().split(',')[0])
                elif isinstance(entry, tk.Entry):
                    entry.delete(0, tk.END)
                
                    
                    
class FormsGUI:
    def __init__(self, form_file, data_file):
        self.form_file= form_file
        self.data_file=data_file
        self.root=tk.Tk()
        self.form = FormConstructor(self.root, self.form_file)
        self.button_next=tk.Button(self.root, text='Next', command=self.next)
        self.button_next.grid(row=self.form.current_row, column=2)
        self.button_show=tk.Button(self.root, text='Show', command=self.show_data)
        self.button_show.grid(row=self.form.current_row,column=3)
        self.root.mainloop()

    def next(self):
        self.form.save_data(self.data_file)
        self.form.clear_form()

    def done(self):
        self.form.save_data(self.data_file)
        self.root.destroy()

    def cancel(self):
        self.root.destroy()
        self.show_data()

    def show_data(self):
        self.root.destroy()

        data=[]
        with open(self.data_file, 'r') as f:
            for line in f:
                data.append(line.strip().split(","))

        self.root=tk.Tk()
        self.root.title('Data')
        self.root.geometry('400x250')

        self.listbox=tk.Listbox(self.root, exportselection=0)
        self.listbox.grid(row=0, column=0)
        self.listbox.config(width=50, height=10)
        
        self.scrollbar=tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        for row in data:
            self.listbox.insert(tk.END, ",".join(row))

        self.button_delete=tk.Button(self.root, text='Delete', command=self.delete)
        self.button_delete.grid(row=1, column=3)
        self.button_done=tk.Button(self.root, text='Done', command=self.done)
        self.button_done.grid(row=2, column=3)
        self.button_revert=tk.Button(self.root, text='Revert', command=self.revert)

    def delete(self):
        self.listbox.delete(tk.ANCHOR)
    def done(self):
        self.root.destroy()

if __name__=='__main__':
    FormsGUI('form.txt', 'output.txt')
