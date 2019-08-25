from tkinter import *
from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog

# Main
root = Tk()
frame = scrolledtext.ScrolledText(root, x=150, y=100)

# First bookmark
def newFile():
    # There is content?
    if len(frame.get('1.0', END+'-1c')) > 0:
        if messagebox.askyesno('Save?','Do You want to save'):
            saveFile()

        else:
            frame.delete('1.0', END)

    root.title(' - New document')

def openFile():
    frame.delete('1.0', END)
    file = filedialog.askopenfile(parent=root, title='Select a text file', filetypes=(('Text file', '*.txt'), ('All files','*.*')))

    if file != None:
        contents = file.read()
        frame.insert('1.0', contents)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode='w')

    if file != None:
        data = frame.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def findInFile():
    # MOZNA JESZCZE INT - SPRAWDZ
    findChars = simpledialog.askstring('Search...', 'Pass characters: ')
    textData = frame.get('1.0', END)

    quantity = textData.upper().count(findChars.upper())

    if textData.upper().count(textData.upper()) > 0:
        label = messagebox.showinfo('Found:', textData + 'occures' + str(quantity))
    else:
        label = messagebox.showinfo('Found:', 'No resut')

    print(textData.upper().count(findChars.upper()))

    if findChars.upper() in textData.upper():
        print(True)

def exit_program():
    if messagebox.showinfo('Exit','Do you want to close?'):
        root.destroy()

# Second bookmark
def helpBookmark():
    pass

# Third bookmark
def editorInfo():
    label = messagebox.showinfo('About','Text editor information\nVersion: 1.03\nOS compilation: 18321.902\nYear: 2019')

# Menu main settings options
menu = Menu(root)
root.config(menu=menu)

# Menu options

# First main bookmark -tabs
bookmark = Menu(menu)
menu.add_cascade(label='File', menu=bookmark)
bookmark.add_command(label='New', command=newFile())
bookmark.add_command(label='Open', command=openFile())
bookmark.add_command(label='Save', command=saveFile())
bookmark.add_command(label='Save', command=saveFile())
bookmark.add_command(label='SaveAs', command=findInFile())
bookmark.add_separator()
bookmark.add_command(label='Page settings')
bookmark.add_command(label='Print')
bookmark.add_separator()
# bookmark.add_command(label='Exit', command=exit_program())

# Second main bookmark -tabs
helpMenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='Show help', command=helpBookmark())

# Third main bookmark -tabs
infoMenu = Menu(menu)
menu.add_cascade(label='Info', menu=infoMenu)
infoMenu.add_command(label='Editor information', command=editorInfo())

# Keep window open
frame.pack()
root.mainloop()