import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox
import ttkbootstrap as ttk
from collections import deque
from Data.game import gameData
from Methods.functions import *

#Creates the coach window
class coach_window(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("Coach Dashboard")
    self.geometry("500x300")
    self.minsize(500, 300)
    self.label_team = ttk.Label(self, text="What team do you want to add to: ").pack(anchor=tk.W, padx=10)
    self.entry_team = ttk.Entry(self)
    self.entry_team.pack(anchor=tk.W, padx=10)
    self.label_coach = ttk.Label(self, text="Enter all the numbers of your player on your team divided by spaces: ").pack(anchor=tk.W, padx=10, pady=10)
    self.entry_coach = ttk.Entry(self)
    self.entry_coach.pack(anchor=tk.W, padx=10)
    self.button_coach = ttk.Button(self, text="Add", command=self.coach_add).pack(anchor=tk.W, padx=10)

    self.menubar = tk.Menu(self)
    self.closebar = tk.Menu(self.menubar, tearoff=0)
    self.closebar.add_command(label="Close", command=self.on_closing )
    self.menubar.add_cascade(menu=self.closebar, label="Close")
    self.config(menu=self.menubar)

  def on_closing(self):
    self.destroy()

  def coach_add(self):
    team_set = self.entry_team.get().lower().strip()
    team_check = check_team_one(team_set)
    if team_check is True:
      data = loadData()

      #takes the team entry and sets it to be able to be checked
      coach_team = self.entry_team.get()
      coach_teamL = coach_team.lower()
      coach_team_trimed = coach_teamL.strip()

      #Gets the list of all the players and splits them up into individual strings.
      coach_num_list = []
      coach_num = self.entry_coach.get()
      coach_num_trimed = coach_num.strip()
      coach_num_list = coach_num.split()

      #checks if the team is in the data
      if coach_team_trimed == "":
        messagebox.showerror(title="Error", message="Please enter a team")
      elif coach_team_trimed in data["teams"]:
        #Iterates through the list of players and adds them
        for x in coach_num_list:
          add_player(coach_team_trimed, x)
        messagebox.showinfo(title="Message", message="Players added")
        self.destroy()
      #If team not in data, it will show a window with the error and clear the team entry
      elif coach_team_trimed not in data["teams"]:
        messagebox.showerror(title="Error", message="Team not found")
        self.entry_team.delete(0, tk.END)
    

class Coach_Choose(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("Coach Choose")
    self.geometry("500x300")
    self.minsize(500, 300)
    self.label = ttk.Label(self, text="Do you want to add to a team or look up a team").pack()
    buttonframe = ttk.Frame(self)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)

    btn1 = ttk.Button(buttonframe, text="Add", command=self.add)
    btn1.grid(row=1, column=0, sticky=tk.W+tk.E)
    btn2 = ttk.Button(buttonframe, text="Look Up", command=self.look_up)
    btn2.grid(row=1, column=1, sticky=tk.W+tk.E)

    buttonframe.pack(fill="x")

  def add(self):
    extrawindow = coach_window()

  def look_up(self):
    extrawindow = Coach_Look_Up()
  

class Coach_Look_Up(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("Coach Choose")
    self.geometry("500x300")
    self.minsize(500, 300)
    self.label = ttk.Label(self, text="What team do you want to search for:").pack()
    self.entry = ttk.Entry(self)
    self.entry.pack()
    self.button = ttk.Button(self, text="Search", command=self.look_up).pack()

  def look_up(self):
    team_set = self.entry.get().lower().strip()
    check_team = check_team_one(team_set)
    if check_team is True:
      data = loadData()
      keys = []
      for key in data["teams"][team_set].keys():
        keys.append(key + ",")
      keys.pop(0)
      messagebox.showinfo(title="Players", message=keys)
        