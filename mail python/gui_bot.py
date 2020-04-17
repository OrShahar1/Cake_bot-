import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox


def gui():
    ROOT = tk.Tk()
    ROOT.withdraw()
    # the input dialog
    USER_INP = simpledialog.askstring(title="Cake BOT",prompt="Cake BOT \n For start bot send \"run\"")
    return USER_INP

def gui_error():
    tkinter.messagebox.showinfo('Error bot', 'error - write run')
    return ()
