import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root = tk.Tk()

canvas1 = tk.Canvas(root, width=600, height=600, bg='gray95', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Image Convertor From JPEG To PNG')
label1.config(font=('Times New Roman', 20))
canvas1.create_window(250,40, window=label1)


def getJPG():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


browseButton_JPG = tk.Button(text="      Import JPG File     ", command=getJPG, bg='black', fg='white',
                             font=('Times New Roman', 15, 'bold'))
canvas1.create_window(250, 200, window=browseButton_JPG)


def convertToPNG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)


saveAsButton_PNG = tk.Button(text='Convert JPG to PNG', command=convertToPNG, bg='black', fg='white',
                             font=('Times New Roman', 15, 'bold'))
canvas1.create_window(250, 280, window=saveAsButton_PNG)

root.mainloop()