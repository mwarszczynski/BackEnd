from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog

# creating object, main window
root = Tk()
textArea = scrolledtext.ScrolledText(root, width=100, height=50)

# Functions
def newFile():
    # There is content?
    if len(textArea.get('1.0', END+'-1c')) > 0:
        if messagebox.askyesno('Save?','Do You want to save'):
            saveFile()

        else:
            textArea.delete('1.0', END)

    root.title(' - New document')

# overwrite an existing file (if not exist, there will be error)
def openFile():
    textArea.delete('1.0', END)
    file = filedialog.askopenfile(parent=root, title='Select a text file', filetypes=(('Text file', '*.txt'), ('All files','*.*')))

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

def findInFile():
    findString = simpledialog.askstring('Find...', 'Enter text: ')
    textData = textArea.get('1.0', END)

    occurances = textData.upper().count(findString.upper())

    if textData.upper().count(findString.upper()) > 0:
        label = messagebox.showinfo('Found:', findString + 'occures' + str(occurances))

    else:
        label = messagebox.showinfo('Found:', 'No resut')

    # count = 0

    print(textData.upper().count(findString.upper()))

    if findString.upper() in textData.upper():
        print(True)

def about():
    label = messagebox.showinfo('About', 'A Python alternative to Notepad')

def exitRoot():
     if messagebox.askyesno('Quit','Are You sure that You want to quit?'):
         root.destroy()

# Menu options
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save",  command=saveFile)
fileMenu.add_command(label="Find",  command=findInFile)
# fileMenu.add_command(label="Save as...")
fileMenu.add_separator()
fileMenu.add_command(label="Page settings")
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitRoot)

helpMenu = Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About", command=about())

textArea.pack()

# Keep window open
root.mainloop()