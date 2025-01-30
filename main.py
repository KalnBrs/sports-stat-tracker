import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from collections import deque
from UI.game_start import game_start
from UI.search_windows import search_window
from UI.coach_windows import Coach_Choose
from UI.dev_window import dev_window

#Creates the window when class is called
def create_window1():
  extrawindow = game_start()

def create_search_window():
  extrawindow = search_window()

def coach_window_button():
  extrawindow =  Coach_Choose()

#When close buttion is clicked then it will close the window
def on_exit():
  if messagebox.askyesno(title="Exit", message="Are you sure you want to exit?"):
    window.destroy()

def dev_open():
  #Login window
  devWindow = dev_window()

# Creates the window at the start and sets theme
window = ttk.Window(themename = 'darkly')
window.title("Start")
window.geometry("350x260")
window.minsize(350, 260)
label_start = ttk.Label(text="Welcome to the Basketball Stat Tracker", style="Label").pack(padx=10, pady=(10, 0))
label_start_ask = ttk.Label(text="Do you want to start or search for a player or team?", style="Label").pack(padx=10, pady=10)

buttonframe = ttk.Frame(window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)

btn1 = ttk.Button(buttonframe, text="Start Game", command=create_window1, style="TButton")
btn1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W+tk.E)
btn2 = ttk.Button(buttonframe, text="Search", command=create_search_window, style="TButton")
btn2.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W+tk.E)

buttonframe.pack(fill="x", padx=10)

label_coach = ttk.Label(text="Click here if you want to add your teams roster:").pack(padx=10, pady=10)
button_coach = ttk.Button(window, text="Coach", command=coach_window_button).pack(padx=10)

buttonframe = ttk.Frame(window)
buttonframe.columnconfigure(0, weight=1)

button_exit = ttk.Button(buttonframe, text="Exit", command=on_exit)
button_exit.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W+tk.E)
button_dev = ttk.Button(buttonframe, text="Dev", command=dev_open)
button_dev.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W+tk.E)

buttonframe.pack(fill="x", padx=10, pady=10)

window.mainloop()