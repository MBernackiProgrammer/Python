from tkinter import *
from webbrowser import Opera

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#4A7A8C')

frame = Frame(ws)
frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

lb = Listbox(
    frame,
    font= (12)
    )
lb.pack(expand=True, fill=BOTH, side=LEFT)

sb = Scrollbar(
    frame, 
    orient=VERTICAL
    )
sb.pack(fill=Y, side=RIGHT)

lb.configure(yscrollcommand=sb.set)
sb.config(command=lb.yview)

var = int()
while True:
    var = var + 1
    Operation = 'opcja nr'
    Operation = Operation + str(var)
    lb.insert(var, Operation)
    if(var > 50):
        break
        



ws.mainloop()