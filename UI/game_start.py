import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox
import ttkbootstrap as ttk
from collections import deque
from Methods.functions import check_team_two
from UI.choose_team import choose_team
from Data.game import gameData
from Methods.functions import change_color

#Creates the window for when game starts
class game_start(tk.Toplevel):
  def __init__ (self):
    super().__init__()
    self.title("Game Start")
    self.geometry("300x150")
    self.minsize(300, 150)
    self.label_home = ttk.Label(self, text="Home").pack()
    self.entry_home = ttk.Entry(self)
    self.entry_home.pack()
    self.label_away = ttk.Label(self, text="Away").pack()
    self.entry_away = ttk.Entry(self)
    self.entry_away.pack()
    self.button_start_game = ttk.Button(self, text="Start Game", command=self.create_window2)
    self.button_start_game.pack()

    self.team_home = ""
    self.team_home_trimed = ""
    self.team_away = ""
    self.team_away_trimed = ""

    self.menubar = tk.Menu(self)
    self.closebar = tk.Menu(self.menubar, tearoff=0)
    self.closebar.add_command(label="Close", command=self.on_closing )
    self.menubar.add_cascade(menu=self.closebar, label="Close")
    self.config(menu=self.menubar)

  def on_closing(self):
    self.destroy()

  def create_window2(self):
    self.team_home = self.entry_home.get()
    team_homeL = self.team_home.lower()
    self.team_home_trimed = team_homeL.strip()

    self.team_away = self.entry_away.get()
    team_awayL = self.team_away.lower()
    self.team_away_trimed = team_awayL.strip()

    gameData.team_home = self.team_home 
    gameData.team_home_trimed = self.team_home_trimed
    gameData.team_away = self.team_away
    gameData.team_away_trimed = self.team_away_trimed

    gameData.homeTimeLeft = 5
    gameData.awayTimeLeft = 5
    gameData.homeFouls = 0
    gameData.awayFouls = 0 

    if self.team_away_trimed != "" and self.team_home_trimed != "":
      if check_team_two(self.team_home_trimed, self.team_away_trimed) is True:
        extrawindow = choose_team()
    else:
      messagebox.showerror(title="Error", message="Please enter a valid team name")
