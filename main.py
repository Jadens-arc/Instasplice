import tkinter as tk
from tkinter import filedialog
from SplitImage_source import autosplit

root = tk.Tk()
root.title('Instasplice')
root.geometry('300x200')

def browseFiles():
    filename = filedialog.askopenfilename(
    	initialdir = "/",
    	title = "Select a File",
    	filetypes = (
			("all files", "*.*"),
    		("JPG files", "*.jpg*"),
    		("PNG files", "*.png*"),
    		("JPEG", "*.jpeg*"),
		)
    )
    return filename

def cropImage():
	path = browseFiles()
	autosplit(path)

      

selectButton = tk.Button(root, text="Select File", command=cropImage)
selectButton.place(relx=0.1, rely=0.4, relwidth=0.8)

root.mainloop()

