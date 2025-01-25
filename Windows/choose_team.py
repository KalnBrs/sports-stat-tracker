import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json
import ttkbootstrap as ttk
from Windows.team_frames import team_frame_home, team_frame_away
from game import gameData
from Methods.functions import change_color

#Creates the window for choose team
class choose_team(tk.Toplevel):
  def __init__ (self):
    super().__init__()
    self.title("Choose Team")
    self.geometry("400x100")
    self.minsize(400, 100)
    self.label_ask = ttk.Label(self, text="Choose a team").pack()
    buttonframe = ttk.Frame(self)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)

    self.clicked = StringVar()
    self.clicked.set("None")

    with open("options.json", "r") as f:
      data = json.load(f)

    self.drop = OptionMenu(self, self.clicked, *data["options"])
    self.drop.pack(pady = 10)

    btn1 = ttk.Button(buttonframe, text=gameData.team_home, command=self.create_window_Home)
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
    btn2 = ttk.Button(buttonframe, text=gameData.team_away, command=self.create_window_Away)
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

    buttonframe.pack(fill='x')

    self.menubar = tk.Menu(self)
    self.closebar = tk.Menu(self.menubar, tearoff=0)
    self.closebar.add_command(label="Close", command=self.on_closing )
    self.menubar.add_cascade(menu=self.closebar, label="Close")
    self.config(menu=self.menubar)

  def on_closing(self):
    self.destroy()

  def create_window_Home(self):
    gameData.homeColor = change_color(self.clicked.get())
    extrawindow = team_frame_home(change_color(self.clicked.get()))

  def create_window_Away(self):
    gameData.awayColor = change_color(self.clicked.get())
    extrawindow = team_frame_away(change_color(self.clicked.get()))
