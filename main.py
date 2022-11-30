import tkinter
from tkinter.ttk import Treeview
import sajatmodul
from sajatmodul import *

window = tkinter.Tk()
window.title("Login App")
window.configure(bg='white')
frame = tkinter.Frame(window)
frame.pack()

treeView = Treeview(frame)
treeView['columns'] = ['FirstName', 'LastName']
treeView.heading('#0', text='')
treeView.column('#0', width=0)
treeView.heading('FirstName', text='FirstName')
treeView.column('FirstName', width=300, anchor='center')
treeView.heading('LastName', text='LastName')
treeView.column('LastName', width=300, anchor='center')
treeView.grid(row=3, column=0, columnspan=2)

label1 = tkinter.Label(frame, text="Előnév: ")
label1.grid(row=0, column=0)

entry1 = tkinter.Entry(frame)
entry1.grid(row=0, column=1)

label2 = tkinter.Label(frame, text="Utónév: ")
label2.grid(row=1, column=0)

entry2 = tkinter.Entry(frame)
entry2.grid(row=1, column=1)

button = tkinter.Button(frame, text="Hozzáadás", command=lambda: [addNewName(treeView, Name(entry1.get(), entry2.get())),
                                                                 saveToFile(treeView),
                                                                  (entry1.delete(0, 'end')),
                                                                  (entry2.delete(0, 'end'))
                                                                  ])
button.grid(row=2, column=0, columnspan=2)


sajatmodul.readFromFile(treeView)
window.mainloop()