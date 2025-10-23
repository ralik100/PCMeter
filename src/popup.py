from tkinter import messagebox


def show_message(self, message):
        #function used for showing info
        messagebox.showinfo(title="PCMeter", message=message)




def show_warning(self, warning):
        #function used for showing warnings
        messagebox.showwarning(title="PCMeter", message=warning)
