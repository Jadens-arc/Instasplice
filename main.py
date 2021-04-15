import tkinter as tk
from tkinter import filedialog
from SplitImage_source import autosplit, saveImages, viewImages

root = tk.Tk()
root.title('Instasplice')
root.geometry('300x200')


def browseFiles():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(
            ("all files", "*.*"),
            ("JPG files", "*.jpg*"),
            ("PNG files", "*.png*"),
            ("JPEG", "*.jpeg*"),
        )
    )
    return filename


def saveImagesGUI(images, name, filetype):
    folder = filedialog.askdirectory()
    print(folder + name)
    saveImages(images, folder + "/" + name, filetype, show=False)


def cropImage():
    path = browseFiles()
    if path:
        images, name, filetype = autosplit(path, save=False)
        viewPhotosBtn = tk.Button(
            root, text="View Photos", command=lambda: viewImages(images))
        viewPhotosBtn.place(relx=0.1, rely=0.5, relwidth=0.8)
        saveImagesBtn = tk.Button(
            root, text="Save Photos", command=lambda: saveImagesGUI(images, name, filetype))
        saveImagesBtn.place(relx=0.1, rely=0.6, relwidth=0.8)


title = tk.Label(root, text="Pick an image to crop")
title.place(relx=0.1, rely=0.3, relwidth=0.8)

selectButton = tk.Button(root, text="Select File", command=cropImage)
selectButton.place(relx=0.1, rely=0.4, relwidth=0.8)

root.mainloop()
