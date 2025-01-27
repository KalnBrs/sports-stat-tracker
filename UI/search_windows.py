import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox
import ttkbootstrap as ttk
from collections import deque
from Data.game import gameData
from Methods.functions import *


#Creates the window for the search
class search_window(tk.Toplevel): 
  def __init__(self):
    super().__init__()
    self.title("Search")
    self.geometry("400x100")
    self.minsize(400, 100)
    self.label_search = ttk.Label(self, text="Do you want to search for player or team satistics?").pack()
    buttonframe = ttk.Frame(self)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)

    btn1 = ttk.Button(buttonframe, text="Player", command=self.create_window_player)
    btn1.grid(row=1, column=0, sticky=tk.W+tk.E)
    btn2 = ttk.Button(buttonframe, text="Team", command=self.create_window_team)
    btn2.grid(row=1, column=1, sticky=tk.W+tk.E)

    buttonframe.pack(fill="x")

    self.menubar = tk.Menu(self)
    self.closebar = tk.Menu(self.menubar, tearoff=0)
    self.closebar.add_command(label="Close", command=self.on_closing )
    self.menubar.add_cascade(menu=self.closebar, label="Close")
    self.config(menu=self.menubar)

  def on_closing(self):
    self.destroy()

  def create_window_player(self):
    window = search_player_window()

  def create_window_team(self):
    window = search_team_window()

#Creates the window for the search for a team
class search_team_window(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("Search for team")
    self.geometry("300x100")
    self.minsize(300, 100)
    self.label_team_search = ttk.Label(self, text="Enter the name of the team you want to search for: ").pack()
    self.entry_team_search = ttk.Entry(self)
    self.entry_team_search.pack()
    self.button_team_search = ttk.Button(self, text="Search", command=self.search_team).pack()

    self.menubar = tk.Menu(self)
    self.closebar = tk.Menu(self.menubar, tearoff=0)
    self.closebar.add_command(label="Close", command=self.on_closing )
    self.menubar.add_cascade(menu=self.closebar, label="Close")
    self.config(menu=self.menubar)

  def on_closing(self):
    self.destroy()

  def search_team(self):
    data = loadData()
    team_search = self.entry_team_search.get().lower().strip()

    if team_search in data["teams"]:
      replace_stats(team_search)
    elif team_search not in data["teams"]:
      messagebox.showerror(title="No team found", message="No team found")
    else:
      print("error Search_team_window")

#Creates the window for the search for a player
class search_player_window(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("Search for Player")
    self.geometry("300x150")
    self.minsize(300, 140)
    self.label_team = ttk.Label(self, text="Team: ").pack()
    self.entry_team = ttk.Entry(self)
    self.entry_team.pack()
    self.label_num = ttk.Label(self, text="Number: ").pack()
    self.entry_num = ttk.Entry(self)
    self.entry_num.pack()
    self.button_search = ttk.Button(self, text="Search", command=self.player_search)
    self.button_search.pack()

    self.menubar = tk.Menu(self)
    self.closebar = tk.Menu(self.menubar, tearoff=0)
    self.closebar.add_command(label="Close", command=self.on_closing )
    self.menubar.add_cascade(menu=self.closebar, label="Close")
    self.config(menu=self.menubar)

  def on_closing(self):
    self.destroy()

  def player_search(self):
    data = loadData()
    global team_trimed
    team = self.entry_team.get()
    teamL = team.lower()
    team_trimed = teamL.strip()
    global ask_num
    ask_num = self.entry_num.get()
    try:
      if team_trimed in data["teams"] and ask_num in data["teams"][team_trimed]:
        window = Search_Stat_Window()
      elif team_trimed not in data["teams"] and ask_num not in data["teams"][team_trimed]:
        messagebox.showinfo(title="Message", message="Team and Player not found")
        self.entry_team.delete(0, tk.END)
        self.entry_num.delete(0, tk.END)
      elif team_trimed not in data["teams"]:
        messagebox.showinfo(title="Message", message="Team not found")
        self.entry_team.delete(0, tk.END)
      elif ask_num not in data["teams"][team_trimed]:
        messagebox.showinfo(title="Messaage", message="Player not found")
        self.entry_num.delete(0, tk.END)
      else:
        print("error 111")
    except KeyError:
      messagebox.showerror(title="Error", message="Team not found")

#Creates the stat window
class Search_Stat_Window(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("Stats")
    self.geometry("530x125")
    self.minsize(530, 125)
    self.label_team = ttk.Label(self, text="What Stat do you want to look up?").pack(pady=10)
    buttonframe = ttk.Frame(self)

    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)
    buttonframe.columnconfigure(3, weight=1)

    bnt1 = ttk.Button(buttonframe, text="2pt Made/missed", command=self.two_point_made_missed)
    bnt1.grid(row=0, column=0, sticky=tk.W+tk.E)
    bnt2 = ttk.Button(buttonframe, text="3pt Made/missed", command=self.three_point_made_missed)
    bnt2.grid(row=0, column=1, sticky=tk.W+tk.E)
    bnt3 = ttk.Button(buttonframe, text="Free Throw Made/missed", command=self.free_throws_made_missed)
    bnt3.grid(row=0, column=2, sticky=tk.W+tk.E)
    bnt4 = ttk.Button(buttonframe, text="Rebounds", command=self.rebound)
    bnt4.grid(row=0, column=3, sticky=tk.W+tk.E)
    bnt5 = ttk.Button(buttonframe, text="Turnovers", command=self.turnover)
    bnt5.grid(row=1, column=0, sticky=tk.W+tk.E)
    bnt6 = ttk.Button(buttonframe, text="Steals", command=self.steal)
    bnt6.grid(row=1, column=1, sticky=tk.W+tk.E)
    bnt7 = ttk.Button(buttonframe, text="Assists", command=self.assist)
    bnt7.grid(row=1, column=2, sticky=tk.W+tk.E)
    bnt8 = ttk.Button(buttonframe, text="Blocks", command=self.block)
    bnt8.grid(row=1, column=3, sticky=tk.W+tk.E)
    bnt9 = ttk.Button(buttonframe, text="Points", command=self.points)
    bnt9.grid(row=2, column=0, sticky=tk.W+tk.E)
    bnt10 = ttk.Button(buttonframe, text="Feild Goals", command=self.feild_goals)
    bnt10.grid(row=2, column=1, sticky=tk.W+tk.E)
    btn11 = ttk.Button(buttonframe, text="All Stats", command=self.all_stats)
    btn11.grid(row=2, column=2, sticky=tk.W+tk.E)
    bnt12 = ttk.Button(buttonframe, text="Cancel Search", command=self.end_game)
    bnt12.grid(row=2, column=3, sticky=tk.W+tk.E)

    buttonframe.pack(fill="x")

    self.menubar = tk.Menu(self)
    self.closebar = tk.Menu(self.menubar, tearoff=0)
    self.closebar.add_command(label="Close", command=self.on_closing )
    self.menubar.add_cascade(menu=self.closebar, label="Close")
    self.config(menu=self.menubar)

  def on_closing(self):
    self.destroy()

  def two_point_made_missed(self):
    stat_search_divide(team_trimed, ask_num, "1", "2")

  def three_point_made_missed(self):
    stat_search_divide(team_trimed, ask_num, "3", "4")

  def free_throws_made_missed(self):
    stat_search_divide(team_trimed, ask_num, "10", "11")

  def rebound(self):
    stat_search_add(team_trimed, ask_num, "5")

  def turnover(self):
    stat_search_add(team_trimed, ask_num, "6")

  def steal(self):
    stat_search_add(team_trimed, ask_num, "7")

  def assist(self):
    stat_search_add(team_trimed, ask_num, "8")

  def block(self):
    stat_search_add(team_trimed, ask_num, "9")

  def points(self):
    stat_search_add(team_trimed, ask_num, "12")

  def feild_goals(self):
    stat_search_add_divide(team_trimed, ask_num)

  def all_stats(self):
    stats_all_player(team_trimed,ask_num)

  def end_game(self):
    self.destroy()

