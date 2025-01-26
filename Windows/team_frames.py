import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox
import ttkbootstrap as ttk
from collections import deque
from game import gameData
from Methods.functions import *
from Windows.stat_window_game import Stat_Window_Game

#Creates the window for the away team
class team_frame_away(tk.Toplevel):
  def __init__ (self, color):
    super().__init__()
    self.title(gameData.team_away)
    self.geometry("500x135")
    self.minsize(500, 135)
    self.configure(background = color)
    self.label_num_away = ttk.Label(self, text="Enter the number number of the player and pick the stat").pack()
    self.entry_num_away = ttk.Entry(self)
    self.entry_num_away.pack()
    buttonframe = ttk.Frame(self)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)
    buttonframe.columnconfigure(3, weight=1)

    bnt1 = ttk.Button(buttonframe, text="Made 2pt", command=self.two_point_made_away)
    bnt1.grid(row=0, column=0, sticky=tk.W+tk.E)
    bnt2 = ttk.Button(buttonframe, text="Missed 2pt", command=self.two_point_missed_away)
    bnt2.grid(row=0, column=1, sticky=tk.W+tk.E)
    bnt3 = ttk.Button(buttonframe, text="Made 3pt", command=self.three_point_made_away)
    bnt3.grid(row=0, column=2, sticky=tk.W+tk.E)
    bnt4 = ttk.Button(buttonframe, text="Missed 3pt", command=self.three_point_missed_away)
    bnt4.grid(row=0, column=3, sticky=tk.W+tk.E)
    bnt5 = ttk.Button(buttonframe, text="Rebound", command=self.rebound_away)
    bnt5.grid(row=1, column=0, sticky=tk.W+tk.E)
    bnt6 = ttk.Button(buttonframe, text="Turnover", command=self.turnover_away)
    bnt6.grid(row=1, column=1, sticky=tk.W+tk.E)
    bnt7 = ttk.Button(buttonframe, text="Steal", command=self.steal_away)
    bnt7.grid(row=1, column=2, sticky=tk.W+tk.E)
    bnt8 = ttk.Button(buttonframe, text="Assist", command=self.assist_away)
    bnt8.grid(row=1, column=3, sticky=tk.W+tk.E)
    bnt9 = ttk.Button(buttonframe, text="Block", command=self.block_away)
    bnt9.grid(row=2, column=0, sticky=tk.W+tk.E)
    bnt10 = ttk.Button(buttonframe, text="Free Throw Made", command=self.free_throw_made_away)
    bnt10.grid(row=2, column=1, sticky=tk.W+tk.E)
    bnt11 = ttk.Button(buttonframe, text="Free Throw Missed", command=self.free_throw_missed_away)
    bnt11.grid(row=2, column=2, sticky=tk.W+tk.E)
    bnt12 = ttk.Button(buttonframe, text="End game", command=self.end_game)
    bnt12.grid(row=2, column=3, sticky=tk.W+tk.E)

    buttonframe.pack(fill="x")

    self.stat_button = ttk.Button(self, text="Stats", command=self.open_stats).pack(padx=5)

    self.menubar = tk.Menu(self)
    self.closebar = tk.Menu(self.menubar, tearoff=0)
    self.closebar.add_command(label="Close", command=self.on_closing )
    self.menubar.add_cascade(menu=self.closebar, label="Close")
    self.config(menu=self.menubar)

  def open_stats(self):
    extra_window = Stat_Window_Game()

  def on_closing(self):
    self.destroy()

  def two_point_made_away(self):
    playerC = check_player(gameData.team_away_trimed, "1")
    if playerC is True:
      stat_points_update("1", 2, gameData.team_away_trimed, "1")
    else:
      print("error 2")

  def three_point_made_away(self):
    playerC = check_player(gameData.team_away_trimed, "1")
    if playerC is True:
      stat_points_update("3", 3, gameData.team_away_trimed, "1")

  def free_throw_made_away(self):
    playerC = check_player(gameData.team_away_trimed, "1")
    if playerC is True:
      stat_points_update("10", 1, gameData.team_away_trimed, "1")

  def two_point_missed_away(self):
    playerC = check_player(gameData.team_away_trimed, "1")
    if playerC is True:
      stat_update("2", gameData.team_away_trimed, "1")

  def three_point_missed_away(self):
    playerC = check_player(gameData.team_away_trimed, "1")
    if playerC is True:
      stat_update("4", gameData.team_away_trimed, "1")

  def rebound_away(self):
    playerC = check_player(gameData.team_away_trimed, "1")
    if playerC is True:
      stat_update("5", gameData.team_away_trimed, "1")

  def turnover_away(self):
    playerC = check_player(gameData.team_away_trimed, "1")
    if playerC is True:
      stat_update("6", gameData.team_away_trimed, "1")

  def steal_away(self):
    playerC = check_player(gameData.team_away_trimed, "1")
    if playerC is True:
      stat_update("7", gameData.team_away_trimed, "1")

  def assist_away(self):
    playerC = check_player(gameData.team_away_trimed, "1")
    if playerC is True:
      stat_update("8", gameData.team_away_trimed, "1")

  def block_away(self):
    playerC = check_player(gameData.team_away_trimed, "1")
    if playerC is True:
      stat_update("9", gameData.team_away_trimed, "1")

  def free_throw_missed_away(self):
    playerC = check_player(gameData.team_away_trimed, "1")
    if playerC is True:
      stat_update("11", gameData.team_away_trimed, "1")

  def end_game(self):
    self.destroy()

#Creates the window for the home team
class team_frame_home(tk.Toplevel):
  def __init__ (self, color):
    super().__init__()
    self.title(gameData.team_home)
    self.geometry("500x135")
    self.minsize(500, 135)
    self.configure(background = color)
    self.label_num_home = ttk.Label(self, text="Enter the number of the player and pick the stat").pack()
    self.entry_num_home = ttk.Entry(self) 
    self.entry_num_home.pack()
    global num_home_frame
    num_home_frame = self.entry_num_home.get()
    buttonframe = ttk.Frame(self)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)
    buttonframe.columnconfigure(3, weight=1)

    bnt1 = ttk.Button(buttonframe, text="Made 2pt", command=self.two_point_made_home)
    bnt1.grid(row=0, column=0, sticky=tk.W+tk.E)
    bnt2 = ttk.Button(buttonframe, text="Missed 2pt", command=self.two_point_missed_home)
    bnt2.grid(row=0, column=1, sticky=tk.W+tk.E)
    bnt3 = ttk.Button(buttonframe, text="Made 3pt", command=self.three_point_made_home)
    bnt3.grid(row=0, column=2, sticky=tk.W+tk.E)
    bnt4 = ttk.Button(buttonframe, text="Missed 3pt", command=self.three_point_missed_home)
    bnt4.grid(row=0, column=3, sticky=tk.W+tk.E)
    bnt5 = ttk.Button(buttonframe, text="Rebound", command=self.rebound_home)
    bnt5.grid(row=1, column=0, sticky=tk.W+tk.E)
    bnt6 = ttk.Button(buttonframe, text="Turnover", command=self.turnover_home)
    bnt6.grid(row=1, column=1, sticky=tk.W+tk.E)
    bnt7 = ttk.Button(buttonframe, text="Steal", command=self.steal_home)
    bnt7.grid(row=1, column=2, sticky=tk.W+tk.E)
    bnt8 = ttk.Button(buttonframe, text="Assist", command=self.assist_home)
    bnt8.grid(row=1, column=3, sticky=tk.W+tk.E)
    bnt9 = ttk.Button(buttonframe, text="Block", command=self.block_home)
    bnt9.grid(row=2, column=0, sticky=tk.W+tk.E)
    bnt10 = ttk.Button(buttonframe, text="Free Throw Made", command=self.free_throw_made_home)
    bnt10.grid(row=2, column=1, sticky=tk.W+tk.E)
    bnt11 = ttk.Button(buttonframe, text="Free Throw Missed", command=self.free_throw_missed_home)
    bnt11.grid(row=2, column=2, sticky=tk.W+tk.E)
    bnt12 = ttk.Button(buttonframe, text="End game", command=self.end_game)
    bnt12.grid(row=2, column=3, sticky=tk.W+tk.E)

    buttonframe.pack(fill="x")

    self.stat_button = ttk.Button(self, text="Stats", command=self.open_stats).pack(padx=5)

    self.menubar = tk.Menu(self)
    self.closebar = tk.Menu(self.menubar, tearoff=0)
    self.closebar.add_command(label="Close", command=self.on_closing )
    self.menubar.add_cascade(menu=self.closebar, label="Close")
    self.config(menu=self.menubar)

  def open_stats(self):
    extra_window = Stat_Window_Game()

  def on_closing(self):
    self.destroy()

  def two_point_made_home(self):
    playerC = check_player(gameData.team_home_trimed, "1")
    if playerC is True:
      stat_points_update("1", 2, gameData.team_home_trimed, "1")
    else:
      print("error 2")

  def three_point_made_home(self):
    playerC = check_player(gameData.team_home_trimed, "1")
    if playerC is True:
      stat_points_update("3", 3, gameData.team_home_trimed, "1")

  def free_throw_made_home(self):
    playerC = check_player(gameData.team_home_trimed, "1")
    if playerC is True:
      stat_points_update("10", 1, gameData.team_home_trimed, "1")

  def two_point_missed_home(self):
    playerC = check_player(gameData.team_home_trimed, "1")
    if playerC is True:
      stat_update("2", gameData.team_home_trimed, "1")

  def three_point_missed_home(self):
    playerC = check_player(gameData.team_home_trimed, "1")
    if playerC is True:
      stat_update("4", gameData.team_home_trimed, "1")

  def rebound_home(self):
    playerC = check_player(gameData.team_home_trimed, "1")
    if playerC is True:
      stat_update("5", gameData.team_home_trimed, "1")

  def turnover_home(self):
    playerC = check_player(gameData.team_home_trimed, "1")
    if playerC is True:
      stat_update("6", gameData.team_home_trimed, "1")

  def steal_home(self):
    playerC = check_player(gameData.team_home_trimed, "1")
    if playerC is True:
      stat_update("7", gameData.team_home_trimed, "1")

  def assist_home(self):
    playerC = check_player(gameData.team_home_trimed, "1")
    if playerC is True:
      stat_update("8", gameData.team_home_trimed, "1")

  def block_home(self):
    playerC = check_player(gameData.team_home_trimed, "1")
    if playerC is True:
      stat_update("9", gameData.team_home_trimed, "1")

  def free_throw_missed_home(self):
    playerC = check_player(gameData.team_home_trimed, "1")
    if playerC is True:
      stat_update("11", gameData.team_home_trimed, "1")

  def end_game(self):
    self.destroy()
