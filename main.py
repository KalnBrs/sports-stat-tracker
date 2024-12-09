import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox
import ttkbootstrap as ttk
from collections import deque

try:
  #Function to use for Procedure
  #Checks if player is in data
  def check_player(team, player):
    if player is not None and player.isdigit():
      check_data_loop = True
      while check_data_loop is True:   
        with open("data.json", "r") as f:
          data = json.load(f)
          if player in data["teams"][team]:
            print("data added")
            check_data_loop = False
            return True
          else:
            add_player(team, player)

    else:
      messagebox.showerror(title="Error", message="Please enter a valid number")

  #Adds player to data
  def add_player(team, num):
    my_player = {
      num: {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "12": 0,
        "13": 0,
        "14": 0     
      }
    }

    with open("data.json", "r") as f:
      data = json.load(f)
      data["teams"][team].update(my_player)

    with open("data.json", "w") as f:
      json.dump(data, f, indent=2)

  #Updates the stats when it is a non point stat
  def stat_update(statT, team, num):
    with open("data.json", "r") as f:
      data = json.load(f)
    data['teams'][team][num][statT] += 1

    with open("data.json", "w") as f:
      f.write(json.dumps(data, indent=4))

  #Updates the stats when it is a point stat
  def stat_points_update(statT, points, team, num):
    with open("data.json", "r") as f:
      data = json.load(f)
    data["teams"][team][num][statT] += 1
    data["teams"][team][num]["12"] += points

    with open("data.json", "w") as f:
      f.write(json.dumps(data, indent=4))

  def stat_search_divide(team, player, num1, num2):
    with open("data.json", "r") as f:
      data = json.load(f)
    messagebox.showinfo(title="Search Found", message=str(data["teams"][team][player][num1]) + "/" + str(data["teams"][team][player][num2] + data["teams"][team][player][num1]))

  def stat_search_add(team, player, stat):
    with open("data.json", "r") as f:
      data = json.load(f)
    if data["teams"][team][player][stat] != 0:
      messagebox.showinfo(title="Search Found", message=data["teams"][team][player][stat])
    elif data["teams"][team][player][stat] == 0:
      messagebox.showinfo(title="Search Found", message="0")
    else:
      messagebox.showerror(title="Error", message="Error")

  def stat_search_add_divide(team, player):
    with open("data.json", "r") as f:
      data = json.load(f)
    sumMade = data["teams"][team][player]["1"] + data["teams"][team][player]["3"]
    sumMissed = sumMade + data["teams"][team][player]["2"] + data["teams"][team][player]["4"]

    messagebox.showinfo(title="Search Found", message=str(sumMade) + "/" + str(sumMissed)) 

  #Shows the stats for the whole team
  def replace_stats(team):
    with open("data.json", "r") as f:
      data = json.load(f)

    two_point_made = 0
    two_point_missed = 0
    three_point_made = 0
    three_point_missed = 0
    rebounds = 0
    turnovers = 0
    steals = 0
    assists = 0
    blocks = 0
    free_throws_made = 0
    free_throws_missed = 0
    points = 0


    for x in data["teams"][team]:
      two_point_made += data["teams"][team][x]["1"]
      two_point_missed += data["teams"][team][x]["2"]
      three_point_made += data["teams"][team][x]["3"]
      three_point_missed += data["teams"][team][x]["4"]
      rebounds += data["teams"][team][x]["5"]
      turnovers += data["teams"][team][x]["6"]
      steals += data["teams"][team][x]["7"]
      assists += data["teams"][team][x]["8"]
      blocks += data["teams"][team][x]["9"]
      free_throws_made += data["teams"][team][x]["10"]
      free_throws_missed += data["teams"][team][x]["11"]
      points += data["teams"][team][x]["12"]

    player = {
        "2pt Made": two_point_made,
        "2pt Missed": two_point_missed,
        "3pt Made": three_point_made,
        "3pt Missed": three_point_missed,
        "Rebounds": rebounds,
        "Turnovers": turnovers,
        "Steals": steals,
        "Assists": assists,
        "Blocks": blocks,
        "Free Throws Made": free_throws_made,
        "Free Throws Missed": free_throws_made,
        "Points": points
    }
    messagebox.showinfo(title="Team Stats", message=json.dumps(player, indent=4))

  #Shows the all the stats for one player
  def stats_all_player(team, player):
    with open("data.json", "r") as f:
      data = json.load(f)

    two_point_made = 0
    two_point_missed = 0
    three_point_made = 0
    three_point_missed = 0
    rebounds = 0
    turnovers = 0
    steals = 0
    assists = 0
    blocks = 0
    free_throws_made = 0
    free_throws_missed = 0
    points = 0

    two_point_made += data["teams"][team][player]["1"]
    two_point_missed += data["teams"][team][player]["2"]
    three_point_made += data["teams"][team][player]["3"]
    three_point_missed += data["teams"][team][player]["4"]
    rebounds += data["teams"][team][player]["5"]
    turnovers += data["teams"][team][player]["6"]
    steals += data["teams"][team][player]["7"]
    assists += data["teams"][team][player]["8"]
    blocks += data["teams"][team][player]["9"]
    free_throws_made += data["teams"][team][player]["10"]
    free_throws_missed += data["teams"][team][player]["11"]
    points += data["teams"][team][player]["12"]

    player_all = {
        "2pt Made": two_point_made,
        "2pt Missed": two_point_missed,
        "3pt Made": three_point_made,
        "3pt Missed": three_point_missed,
        "Rebounds": rebounds,
        "Turnovers": turnovers,
        "Steals": steals,
        "Assists": assists,
        "Blocks": blocks,
        "Free Throws Made": free_throws_made,
        "Free Throws Missed": free_throws_made,
        "Points": points
    }

    messagebox.showinfo(title="Player Stats", message=json.dumps(player_all, indent=4))

  #Checks if a single team is in the data
  def check_team_one(team):
    check_data_loop = True
    while check_data_loop is True:
      with open("data.json", "r") as f:
        data = json.load(f)
      check_data_loop = False
      if team in data["teams"]:
        return True
      elif team not in data["teams"]:
        if messagebox.askyesno(title="Team Not Found", message="Team Not Found Would You Like To Add It?"):
          add_team(team)
          check_data_loop = True
        else:
          messagebox.showinfo(title="Message", message="team not added")
      else:
        print("error 302")
        check_data_loop = True

  #Checks if two teams are in the data
  def check_team_two(teamH, teamA):
    with open("data.json", "r") as f:
      data = json.load(f)
    check_data_loop = True
    while check_data_loop is True:
      with open("data.json", "r") as f:
        data = json.load(f)
      if teamH in data["teams"] and teamA in data["teams"]:
        check_data_loop = False
        return True
      elif teamH not in data["teams"] and teamA not in data["teams"]:
        check_data_loop = False
        add_team(teamA)
        add_team(teamH)
        return True
      elif teamH in data["teams"]:
        add_team(teamA) 
        print("added away team")
      elif teamA in data["teams"]:
        add_team(teamH)
        print("added home team")
      else:
        print("error 1") 
    with open("data.json", "w") as f:
      f.write(json.dumps(data, indent=4))

  #Adds a team into the data
  def add_team(team_name):
    num = "player"
    my_team = {
      team_name: {
        num: {
          "1": 0,
          "2": 0,
          "3": 0,
          "4": 0,
          "5": 0,
          "6": 0,
          "7": 0,
          "8": 0,
          "9": 0,
          "10": 0,
          "11": 0,
          "12": 0,
          "13": 0,
          "14": 0     
        }
      }
    }
    with open("data.json", "r") as f:
      data = json.load(f)
      data["teams"].update(my_team)

    with open("data.json", "w") as f:
      f.write(json.dumps(data, indent=2))

  def add_color(color, colorValue):
    with open("options.json", "r") as f:
      optionsList = json.load(f)

    optionsList[options].append(color, 0)
    optionsList[options][color] = colorValue

    with open("options.json", "w") as f:
      f.write(json.dumps(optionsList, indent=2))

  def change_color(color) -> str:
    with open("options.json", "r") as f:
      colors = json.load(f)

    if color in colors["color-values"]:
      return colors["color-values"][color]
    else:
      return color

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

      self.menubar = tk.Menu(self)
      self.closebar = tk.Menu(self.menubar, tearoff=0)
      self.closebar.add_command(label="Close", command=self.on_closing )
      self.menubar.add_cascade(menu=self.closebar, label="Close")
      self.config(menu=self.menubar)

    def on_closing(self):
      self.destroy()

    def create_window2(self):
      global team_home
      global team_home_trimed
      team_home = self.entry_home.get()
      team_homeL = team_home.lower()
      team_home_trimed = team_homeL.strip()
      global team_away
      global team_away_trimed
      team_away = self.entry_away.get()
      team_awayL = team_away.lower()
      team_away_trimed = team_awayL.strip()
      if team_away_trimed != "" and team_home_trimed != "":
        if check_team_two(team_home_trimed, team_away_trimed) is True:
          extrawindow = choose_team()
      else:
        messagebox.showerror(title="Error", message="Please enter a valid team name")


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

      btn1 = ttk.Button(buttonframe, text=team_home, command=self.create_window_Home)
      btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
      btn2 = ttk.Button(buttonframe, text=team_away, command=self.create_window_Away)
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
      extrawindow = team_frame_home(change_color(self.clicked.get()))

    def create_window_Away(self):
      extrawindow = team_frame_away(change_color(self.clicked.get()))


  #Creates the window for the home team
  class team_frame_home(tk.Toplevel):
    def __init__ (self, color):
      super().__init__()
      self.title(team_home)
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
      playerC = check_player(team_home_trimed, self.entry_num_home.get())
      if playerC is True:
        stat_points_update("1", 2, team_home_trimed, self.entry_num_home.get())
      else:
        print("error 2")

    def three_point_made_home(self):
      playerC = check_player(team_home_trimed, self.entry_num_home.get())
      if playerC is True:
        stat_points_update("3", 3, team_home_trimed, self.entry_num_home.get())

    def free_throw_made_home(self):
      playerC = check_player(team_home_trimed, self.entry_num_home.get())
      if playerC is True:
        stat_points_update("10", 1, team_home_trimed, self.entry_num_home.get())

    def two_point_missed_home(self):
      playerC = check_player(team_home_trimed, self.entry_num_home.get())
      if playerC is True:
        stat_update("2", team_home_trimed, self.entry_num_home.get())

    def three_point_missed_home(self):
      playerC = check_player(team_home_trimed, self.entry_num_home.get())
      if playerC is True:
        stat_update("4", team_home_trimed, self.entry_num_home.get())

    def rebound_home(self):
      playerC = check_player(team_home_trimed, self.entry_num_home.get())
      if playerC is True:
        stat_update("5", team_home_trimed, self.entry_num_home.get())

    def turnover_home(self):
      playerC = check_player(team_home_trimed, self.entry_num_home.get())
      if playerC is True:
        stat_update("6", team_home_trimed, self.entry_num_home.get())

    def steal_home(self):
      playerC = check_player(team_home_trimed, self.entry_num_home.get())
      if playerC is True:
        stat_update("7", team_home_trimed, self.entry_num_home.get())

    def assist_home(self):
      playerC = check_player(team_home_trimed, self.entry_num_home.get())
      if playerC is True:
        stat_update("8", team_home_trimed, self.entry_num_home.get())

    def block_home(self):
      playerC = check_player(team_home_trimed, self.entry_num_home.get())
      if playerC is True:
        stat_update("9", team_home_trimed, self.entry_num_home.get())

    def free_throw_missed_home(self):
      playerC = check_player(team_home_trimed, self.entry_num_home.get())
      if playerC is True:
        stat_update("11", team_home_trimed, self.entry_num_home.get())

    def end_game(self):
      self.destroy()


  #Creates the window for the away team
  class team_frame_away(tk.Toplevel):
    def __init__ (self, color):
      super().__init__()
      self.title(team_away)
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
      playerC = check_player(team_away_trimed, self.entry_num_away.get())
      if playerC is True:
        stat_points_update("1", 2, team_away_trimed, self.entry_num_away.get())
      else:
        print("error 2")

    def three_point_made_away(self):
      playerC = check_player(team_away_trimed, self.entry_num_away.get())
      if playerC is True:
        stat_points_update("3", 3, team_away_trimed, self.entry_num_away.get())

    def free_throw_made_away(self):
      playerC = check_player(team_away_trimed, self.entry_num_away.get())
      if playerC is True:
        stat_points_update("10", 1, team_away_trimed, self.entry_num_away.get())

    def two_point_missed_away(self):
      playerC = check_player(team_away_trimed, self.entry_num_away.get())
      if playerC is True:
        stat_update("2", team_away_trimed, self.entry_num_away.get())

    def three_point_missed_away(self):
      playerC = check_player(team_away_trimed, self.entry_num_away.get())
      if playerC is True:
        stat_update("4", team_away_trimed, self.entry_num_away.get())

    def rebound_away(self):
      playerC = check_player(team_away_trimed, self.entry_num_away.get())
      if playerC is True:
        stat_update("5", team_away_trimed, self.entry_num_away.get())

    def turnover_away(self):
      playerC = check_player(team_away_trimed, self.entry_num_away.get())
      if playerC is True:
        stat_update("6", team_away_trimed, self.entry_num_away.get())

    def steal_away(self):
      playerC = check_player(team_away_trimed, self.entry_num_away.get())
      if playerC is True:
        stat_update("7", team_away_trimed, self.entry_num_away.get())

    def assist_away(self):
      playerC = check_player(team_away_trimed, self.entry_num_away.get())
      if playerC is True:
        stat_update("8", team_away_trimed, self.entry_num_away.get())

    def block_away(self):
      playerC = check_player(team_away_trimed, self.entry_num_away.get())
      if playerC is True:
        stat_update("9", team_away_trimed, self.entry_num_away.get())

    def free_throw_missed_away(self):
      playerC = check_player(team_away_trimed, self.entry_num_away.get())
      if playerC is True:
        stat_update("11", team_away_trimed, self.entry_num_away.get())

    def end_game(self):
      self.destroy()


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
      with open("data.json", "r") as f:
        data = json.load(f)
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
      with open("data.json", "r") as f:
        data = json.load(f)
      global team_trimed
      team = self.entry_team.get()
      teamL = team.lower()
      team_trimed = teamL.strip()
      global ask_num
      ask_num = self.entry_num.get()
      try:
        if team_trimed in data["teams"] and ask_num in data["teams"][team_trimed]:
          window = stat_window()
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
  class stat_window(tk.Toplevel):
    def __init__(self, color):
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
        #Sets data.json as data
        with open("data.json", "r") as f:
          data = json.load(f)

        #takes the team entry and sets it to be able to be checked
        coach_team = self.entry_team.get()
        coach_teamL = coach_team.lower()
        coach_team_trimed = coach_teamL.strip()

        #Gets the list of all the players and splits them up into individual strings.
        coach_num_list = []
        coach_num = self.entry_coach.get()
        coach_num_trimed = coach_num.strip()
        coach_num_list = coach_num.split()
        print(coach_num_trimed)

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
        else:
          #No input
          print("error 11")
      

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
        with open("data.json", "r") as f:
          data = json.load(f)
        keys = []
        for key in data["teams"][team_set].keys():
          keys.append(key + ",")
        keys.pop(0)
        messagebox.showinfo(title="Players", message=keys)
          

  class Stat_Window_Game(tk.Toplevel):
    def __init__(self):
      super().__init__()
      self.title("Stats")
      self.geometry("500x500")
      self.minsize(200, 350)

      self.teamHome = StringVar()
      self.teamHome.set(team_home)

      self.teamAway = StringVar()
      self.teamAway.set(team_away)

      self.twoMadeHome = StringVar()
      self.twoMissedHome = StringVar()
      self.threeMadeHome = StringVar()
      self.threeMissedHome = StringVar()
      self.reboundsHome = StringVar()
      self.turnoversHome = StringVar()
      self.stealHome = StringVar()
      self.assistsHome = StringVar()
      self.blocksHome = StringVar()
      self.freeTrowsMadeHome = StringVar()
      self.freeThrowsMissedHome = StringVar()
      self.pointsHome = StringVar()

      self.twoMadeAway = StringVar()
      self.twoMissedAway = StringVar()
      self.threeMadeAway = StringVar()
      self.threeMissedAway = StringVar()
      self.reboundsAway = StringVar()
      self.turnoversAway = StringVar()
      self.stealAway = StringVar()
      self.assistsAway = StringVar()
      self.blocksAway = StringVar()
      self.freeTrowsMadeAway = StringVar()
      self.freeThrowsMissedAway = StringVar()
      self.pointsAway = StringVar()


      #Title
      titleFrame = ttk.Frame(self)
      titleFrame.columnconfigure(0, weight=1)

      self.homeTeamLabel = ttk.Label(titleFrame, text=self.teamHome.get()).grid(column=0, row=0, padx=15)
      self.awayTeamLabel = ttk.Label(titleFrame, text=self.teamAway.get()).grid(column=1, row=0, padx=15)

      titleFrame.pack(pady=(10, 0))


      statsFrame = ttk.Frame(self)
      statsFrame.columnconfigure(0, weight=1)
      statsFrame.columnconfigure(1, weight=1)
      statsFrame.columnconfigure(2, weight=1)
      statsFrame.columnconfigure(3, weight=1)
      statsFrame.columnconfigure(4, weight=1)
      statsFrame.columnconfigure(5, weight=1)
      statsFrame.columnconfigure(6, weight=1)
      statsFrame.columnconfigure(7, weight=1)
      statsFrame.columnconfigure(8, weight=1)
      statsFrame.columnconfigure(9, weight=1)
      statsFrame.columnconfigure(10, weight=1)
      statsFrame.columnconfigure(11, weight=1)
      statsFrame.columnconfigure(12, weight=1)

      #Home Team
      self.twoHH = ttk.Label(statsFrame, text="Reload")
      self.twoHH.grid(column=0, row=1, sticky=tk.E)

      self.twoMH = ttk.Label(statsFrame, text="Reload")
      self.twoMH.grid(column=0, row=2, sticky=tk.E)

      self.threeHH = ttk.Label(statsFrame, text="Reload")
      self.threeHH.grid(column=0, row=3, sticky=tk.E)

      self.threeMH = ttk.Label(statsFrame, text="Reload")
      self.threeMH.grid(column=0, row=4, sticky=tk.E)

      self.rebH = ttk.Label(statsFrame, text="Reload")
      self.rebH.grid(column=0, row=5, sticky=tk.E)

      self.turnH = ttk.Label(statsFrame, text="Reload")
      self.turnH.grid(column=0, row=6, sticky=tk.E)

      self.stealH = ttk.Label(statsFrame, text="Reload")
      self.stealH.grid(column=0, row=7, sticky=tk.E)

      self.assistH = ttk.Label(statsFrame, text="Reload")
      self.assistH.grid(column=0, row=8, sticky=tk.E)

      self.blockH = ttk.Label(statsFrame, text="Reload")
      self.blockH.grid(column=0, row=9, sticky=tk.E)

      self.ftHH = ttk.Label(statsFrame, text="Reload")
      self.ftHH.grid(column=0,row=10, sticky=tk.E)

      self.ftMH = ttk.Label(statsFrame, text="Reload")
      self.ftMH.grid(column=0,row=11, sticky=tk.E)

      self.pointH = ttk.Label(statsFrame, text="Reload")
      self.pointH.grid(column=0,row=12, sticky=tk.E)

      #Away Team
      self.twoHA = ttk.Label(statsFrame, text="Reload")
      self.twoHA.grid(column=2, row=1, sticky=tk.W)

      self.twoMA = ttk.Label(statsFrame, text="Reload")
      self.twoMA.grid(column=2, row=2, sticky=tk.W)

      self.threeHA = ttk.Label(statsFrame, text="Reload")
      self.threeHA.grid(column=2, row=3, sticky=tk.W)

      self.threeMA = ttk.Label(statsFrame, text="Reload")
      self.threeMA.grid(column=2, row=4, sticky=tk.W)

      self.rebA = ttk.Label(statsFrame, text="Reload")
      self.rebA.grid(column=2, row=5, sticky=tk.W)

      self.turnA = ttk.Label(statsFrame, text="Reload")
      self.turnA.grid(column=2, row=6, sticky=tk.W)

      self.stealA = ttk.Label(statsFrame, text="Reload")
      self.stealA.grid(column=2, row=7, sticky=tk.W)

      self.assistA = ttk.Label(statsFrame, text="Reload")
      self.assistA.grid(column=2, row=8, sticky=tk.W)

      self.blockA = ttk.Label(statsFrame, text="Reload")
      self.blockA.grid(column=2, row=9, sticky=tk.W)

      self.ftHA = ttk.Label(statsFrame, text="Reload")
      self.ftHA.grid(column=2, row=10, sticky=tk.W)

      self.ftMA = ttk.Label(statsFrame, text="Reload")
      self.ftMA.grid(column=2, row=11, sticky=tk.W)

      self.pointA = ttk.Label(statsFrame, text="Reload")
      self.pointA.grid(column=2, row=12, sticky=tk.W)

      self.twoMade = ttk.Label(statsFrame, text=": Two point made :").grid(column=1, row=1)
      self.twoMade = ttk.Label(statsFrame, text=": Two point missed :").grid(column=1, row=2)
      self.twoMade = ttk.Label(statsFrame, text=": Three point made :").grid(column=1, row=3)
      self.twoMade = ttk.Label(statsFrame, text=": Three point missed :").grid(column=1, row=4)
      self.twoMade = ttk.Label(statsFrame, text=": Rebounds :").grid(column=1, row=5)
      self.twoMade = ttk.Label(statsFrame, text=": Turnovers :").grid(column=1, row=6)
      self.twoMade = ttk.Label(statsFrame, text=": Steal :").grid(column=1, row=7)
      self.twoMade = ttk.Label(statsFrame, text=": Assist :").grid(column=1, row=8)
      self.twoMade = ttk.Label(statsFrame, text=": Block :").grid(column=1, row=9)
      self.twoMade = ttk.Label(statsFrame, text=": Free throw made :").grid(column=1, row=10)
      self.twoMade = ttk.Label(statsFrame, text=": Free throw missed :").grid(column=1, row=11)
      self.twoMade = ttk.Label(statsFrame, text=": Total Points :").grid(column=1, row=12)

      

      statsFrame.pack(fill="x", anchor=CENTER, padx=10, pady=10)

      def set_variables():
        print("set")
        with open("data.json", "r") as f:
          data = json.load(f)

        twoMadeHomeInt = 0
        twoMissedHomeInt = 0
        threeMadeHomeInt = 0
        threeMissedHomeInt = 0
        reboundsHomeInt = 0
        turnoversHomeInt = 0
        stealHomeInt = 0
        assistsHomeInt = 0
        blocksHomeInt = 0
        freeTrowsMadeHomeInt = 0
        freeThrowsMissedHomeInt = 0
        pointsHomeInt = 0

        twoMadeAwayInt = 0
        twoMissedAwayInt = 0
        threeMadeAwayInt = 0
        threeMissedAwayInt = 0
        reboundsAwayInt = 0
        turnoversAwayInt = 0
        stealAwayInt = 0
        assistsAwayInt = 0
        blocksAwayInt = 0
        freeTrowsMadeAwayInt = 0
        freeThrowsMissedAwayInt = 0
        pointsAwayInt = 0

        for x in data["teams"][team_home_trimed]:

          twoMadeHomeInt += data["teams"][team_home_trimed][x]["1"]
          twoMissedHomeInt += data["teams"][team_home_trimed][x]["2"]
          threeMadeHomeInt += data["teams"][team_home_trimed][x]["3"]
          threeMissedHomeInt += data["teams"][team_home_trimed][x]["4"]
          reboundsHomeInt += data["teams"][team_home_trimed][x]["5"]
          turnoversHomeInt += data["teams"][team_home_trimed][x]["6"]
          stealHomeInt += data["teams"][team_home_trimed][x]["7"]
          assistsHomeInt += data["teams"][team_home_trimed][x]["8"]
          blocksHomeInt += data["teams"][team_home_trimed][x]["9"]
          freeTrowsMadeHomeInt += data["teams"][team_home_trimed][x]["10"]
          freeThrowsMissedHomeInt += data["teams"][team_home_trimed][x]["11"]
          pointsHomeInt += data["teams"][team_home_trimed][x]["12"]

        for x in data["teams"][team_away_trimed]:
          twoMadeAwayInt += data["teams"][team_away_trimed][x]["1"]
          twoMissedAwayInt += data["teams"][team_away_trimed][x]["2"]
          threeMadeAwayInt += data["teams"][team_away_trimed][x]["3"]
          threeMissedAwayInt += data["teams"][team_away_trimed][x]["4"]
          reboundsAwayInt += data["teams"][team_away_trimed][x]["5"]
          turnoversAwayInt += data["teams"][team_away_trimed][x]["6"]
          stealAwayInt += data["teams"][team_away_trimed][x]["7"]
          assistsAwayInt += data["teams"][team_away_trimed][x]["8"]
          blocksAwayInt += data["teams"][team_away_trimed][x]["9"]
          freeTrowsMadeAwayInt += data["teams"][team_away_trimed][x]["10"]
          freeThrowsMissedAwayInt += data["teams"][team_away_trimed][x]["11"]
          pointsAwayInt += data["teams"][team_away_trimed][x]["12"]


        self.twoMadeHome.set(str(twoMadeHomeInt))
        self.twoMissedHome.set(str(twoMissedHomeInt))
        self.threeMadeHome.set(str(threeMadeHomeInt))
        self.threeMissedHome.set(str(threeMissedHomeInt))
        self.reboundsHome.set(str(reboundsHomeInt))
        self.turnoversHome.set(str(turnoversHomeInt))
        self.stealHome.set(str(stealHomeInt))
        self.assistsHome.set(str(assistsHomeInt))
        self.blocksHome.set(str(blocksHomeInt))
        self.freeTrowsMadeHome.set(str(freeTrowsMadeHomeInt))
        self.freeThrowsMissedHome.set(str(freeThrowsMissedHomeInt))
        self.pointsHome.set(str(pointsHomeInt))

        self.twoMadeAway.set(str(twoMadeAwayInt))
        self.twoMissedAway.set(str(twoMissedAwayInt))
        self.threeMadeAway.set(str(threeMadeAwayInt))
        self.threeMissedAway.set(str(threeMissedAwayInt))
        self.reboundsAway.set(str(reboundsAwayInt))
        self.turnoversAway.set(str(turnoversAwayInt))
        self.stealAway.set(str(stealAwayInt))
        self.assistsAway.set(str(assistsAwayInt))
        self.blocksAway.set(str(blocksAwayInt))
        self.freeTrowsMadeAway.set(str(freeTrowsMadeAwayInt))
        self.freeThrowsMissedAway.set(str(freeThrowsMissedAwayInt))
        self.pointsAway.set(str(pointsAwayInt))

        self.twoHH.config(text=self.twoMadeHome.get())
        self.twoMH.config(text=self.twoMissedHome.get())
        self.threeHH.config(text=self.threeMadeHome.get())
        self.threeMH.config(text=self.threeMissedHome.get())
        self.rebH.config(text=self.reboundsHome.get())
        self.turnH.config(text=self.turnoversHome.get())
        self.stealH.config(text=self.stealHome.get())
        self.assistH.config(text=self.assistsHome.get())
        self.blockH.config(text=self.blocksHome.get())
        self.ftHH.config(text=self.freeTrowsMadeHome.get())
        self.ftMH.config(text=self.freeThrowsMissedHome.get())
        self.pointH.config(text=self.pointsHome.get())

        self.twoHA.config(text=self.twoMadeAway.get())
        self.twoMA.config(text=self.twoMissedAway.get())
        self.threeHA.config(text=self.threeMadeAway.get())
        self.threeMA.config(text=self.threeMissedAway.get())
        self.rebA.config(text=self.reboundsAway.get())
        self.turnA.config(text=self.turnoversAway.get())
        self.stealA.config(text=self.stealAway.get())
        self.assistA.config(text=self.assistsAway.get())
        self.blockA.config(text=self.blocksAway.get())
        self.ftHA.config(text=self.freeTrowsMadeAway.get())
        self.ftMA.config(text=self.freeThrowsMissedAway.get())
        self.pointA.config(text=self.pointsAway.get())

      self.reload = ttk.Button(self, text="Reload", command=set_variables).pack()
      self.mainloop()

  class Dev_Window(tk.Toplevel):
    
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

  def dev_window():
    #Login window
    devWindow = Dev_Window()

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
  button_dev = ttk.Button(buttonframe, text="Dev", command=dev_window)
  button_dev.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W+tk.E)

  buttonframe.pack(fill="x", padx=10, pady=10)

  window.mainloop()
  
finally:
  #If the program closes unexpectly 
  print("Program Terminted")
