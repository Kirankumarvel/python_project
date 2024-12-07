# Importing Libraries
# -*- coding: utf-8 -*-
from tkinter import Tk, END, Entry, N, E, S, W, Button
from tkinter import font
from tkinter import Label
from functools import partial

# Defining Helper Functions
def get_input(entry, argu):
    """Insert input into the entry field."""
    entry.insert(END, argu)

def backspace(entry):
    """Remove the last character from the entry field."""
    if entry.get():  # Check if entry is not empty
        entry.delete(len(entry.get()) - 1)

def clear(entry):
    """Clear the entry field."""
    entry.delete(0, END)

def calc(entry):
    """Evaluate the expression in the entry field."""
    input_info = entry.get()
    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg("Cannot divide by 0! Enter valid values.")
        output = ""
    except Exception:  # Catch any other exceptions
        output = "Error"
    clear(entry)
    entry.insert(END, output)

def popupmsg(message):
    """Display a popup message."""
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry("200x100")
    popup.title("Alert")
    label = Label(popup, text=message)
    label.pack(side="top", fill="x", pady=10)
    button_ok = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
    button_ok.pack()

def create_button(root, text, command, row, column, colspan=1):
    """Helper function to create a button."""
    button = Button(root, text=text, padx=10, pady=3,
                    command=command)
    button.grid(row=row, column=column, columnspan=colspan,
                sticky=N + S + E + W)
    return button

# Main Calculator Function
def cal():
    root = Tk()
    root.title("Calculator")
    root.resizable(0, 0)

    # Creating Input Field
    entry_font = font.Font(size=15)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4,
               sticky=N + W + S + E, padx=5, pady=5)

    # Defining Button Colors and Styles
    cal_button_bg = '#FF6600'
    num_button_bg = '#4B4B4B'

    # Creating Buttons
    buttons = [
        ('7', lambda: get_input(entry, '7'), 2, 0),
        ('8', lambda: get_input(entry, '8'), 2, 1),
        ('9', lambda: get_input(entry, '9'), 2, 2),
        ('/', lambda: get_input(entry, '/'), 1, 3),
        ('4', lambda: get_input(entry, '4'), 3, 0),
        ('5', lambda: get_input(entry, '5'), 3, 1),
        ('6', lambda: get_input(entry, '6'), 3, 2),
        ('*', lambda: get_input(entry,'*'), 2 ,3),
        ('1', lambda: get_input(entry,'1'), 4 ,0),
        ('2', lambda: get_input(entry,'2'), 4 ,1),
        ('3', lambda: get_input(entry,'3'), 4 ,2),
        ('-', lambda: get_input(entry,'-'), 3 ,3),
        ('0', lambda: get_input(entry,'0'), 5 ,0),
        ('.', lambda: get_input(entry,'.'), 5 ,1),
        ('+', lambda: get_input(entry,'+'), 4 ,3),
        ('C', lambda: clear(entry), 1 ,2),      # Clear button at (1,2)
        ('<-', lambda: backspace(entry), 1 ,0), # Backspace button at (1,0) 
        ('=', lambda: calc(entry), 5 ,3), 
        ('^', lambda: get_input(entry,'**'), 5 ,2), 
        ('Quit', quit_app ,6 ,1) 
      ]

    # Creating and placing buttons in grid layout
    for (text , command , row , col) in buttons:
        create_button(root,text ,command,row,col)

    root.mainloop()

# Quit Functionality
def quit_app():
   """Quit the application."""
   root.destroy()  # Use destroy instead of quit

# Running the Application
if __name__ == '__main__':
   cal()
