# Description: This is a python program GUI for a chat system

# library
from tkinter import *

# Create the tkinter object (this represents the parent window)

root = Tk()

# Give window a title
root.title('Simple Chat')

# Give window some dimensions
root.geometry('400x500')

# Create a main menu bar
main_menu = Menu(root)

# Create the sub menu
file_menu = Menu(root)
file_menu.add_command(label='New...')
file_menu.add_command(label='Save As...')
file_menu.add_command(label='Exit')

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_command(label='Edit')
root.config(menu=main_menu)

# Create chat window
chatWindow = Text(root, bd=1, bg='black', width=50, height=8)
chatWindow.place(x=6, y=6, height=385, width=370)

# Create message window (where user inputs their msg)
messageWindow = Text(root, bg='white', width=30, height=4, font=('Arial', 12))
messageWindow.place(x=128, y=400, height=88, width=260)

# Create submit button for sending msg
Button = Button(root, text='Send', bg='white', activebackground='light blue', width=12, height=5, font=('Arial', 20))
Button.place(x=6, y=400, height=88, width=120)

# Add scrollbar
Scrollbar = Scrollbar(root, command=chatWindow.yview())
Scrollbar.place(x=375, y=5, height=385)

root.mainloop()