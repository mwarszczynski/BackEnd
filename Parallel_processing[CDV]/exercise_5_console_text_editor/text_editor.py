from tkinter import Tk, scrolledtext, Menu, filedialog, END

# creating object, main window
root = Tk()
textArea = scrolledtext.ScrolledText(root, width=100, height=50)

# Functions
def openFile():
    file = filedialog.askopenfile(parent=root, mode='rb', title='Select a text file')

    if file != None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode='w')

    if file != None:
        # slice off the last character from get, as an extra return (enter) is added.
        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()

# Menu options
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="New")
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save",  command=saveFile)
fileMenu.add_command(label="Save as...")
fileMenu.add_separator()
fileMenu.add_command(label="Page settings")
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

helpMenu = Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About")

textArea.pack()

# Keep window open
root.mainloop()