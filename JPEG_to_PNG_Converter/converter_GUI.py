import tkinter as tk
from tkinter import filedialog
from PIL import Image
#Importing Libraries

#tkinter: This is a standard Python library for creating GUI applications. It provides tools to create windows, buttons, labels, and other GUI elements.
#filedialog: A submodule of Tkinter that provides dialogs for opening and saving files.
#PIL (Python Imaging Library): Specifically, the Image module from Pillow, which is used for opening, manipulating, and saving image files.

root = tk.Tk()   # Tkinter window initialized
root.title('Converter')     # Title of the window

#Creating a Canvas
canvas1 = tk.Canvas(root, width=300, height=250, bg='orange', relief='raised')
canvas1.pack()

#Adding a Label
label1 = tk.Label(root, text='File Converter', bg='lightsteelblue2')   # giving a title to the screen
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

#Variable Initialization
im1 = None  # variable to store path of image


#Defining Functions to Get JPEG File
def getJPG():
    '''Function to get image location and open it with pillow'''
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


font = ('helvetica', 12, 'bold')
bg = 'royalblue'
fg = 'white'
browseButton_JPG = tk.Button(text="      Import JPEG File     ", command=getJPG, bg=bg, fg=fg, font=font)   # Browse button
canvas1.create_window(150, 130, window=browseButton_JPG)

#Function to Convert JPEG to PNG
def convertToPNG():
    '''Function to change file extenstion to png and save it to User's prefered location '''
    global im1
    if im1 is None:
        tk.messagebox.showerror("Error", "No File selected")
    else:
        export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
        im1.save(export_file_path)


saveAsButton_PNG = tk.Button(text='Convert JPEG to PNG', command=convertToPNG, bg=bg, fg=fg, font=font)      # Convert button
canvas1.create_window(150, 180, window=saveAsButton_PNG)
root.mainloop()