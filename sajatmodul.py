from tkinter import messagebox

class Name:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

def saveToFile(treeView):

    try:
        with open("data.txt", "w") as file:
            for row in treeView.get_children():
                file.write(treeView.item(row)['values'][0] + "," + treeView.item(row)['values'][1] + "\n")
    except Exception:
        messagebox.showinfo("SaveFile", "File couldn't be saved")


def addNewName(treeView, name):
    if name.firstName == "" or name.lastName == "":
        messagebox.showinfo("Input", "The first or last name is missing!")
    else:
        treeView.insert('', 'end', values=(name.firstName, name.lastName))


def readFromFile(treeView):
    try:
        file = open("data.txt", "r")
        for row in treeView.get_children():
            treeView.delete(row)
        for row in file:
            strippedRow = row.strip('\n')
            name = strippedRow.split(',', 1)
            treeView.insert('', 'end', values=(name[0], name[1]))
        file.close()
    except Exception:
        messagebox.showinfo("OpenFile", "File couldn't be read")