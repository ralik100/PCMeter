from tkinter import messagebox


def show_message(message):
        #function used for showing info
        messagebox.showinfo(title="PCMeter", message=message)




def show_warning(warning):
        #function used for showing warnings
        messagebox.showwarning(title="PCMeter", message=warning)
