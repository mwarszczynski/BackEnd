from tkinter import *
import tkinter.scrolledtext as ScrolledText

# creating object, main window
root = Tk()
textArea = ScrolledText.ScrolledText(root, width=100, height=50)

# Menu options
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save as...")
fileMenu.add_separator()
fileMenu.add_command(label="Page settings")
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")


textArea.pack()

# Keep window open
root.mainloop()