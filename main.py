import tkinter as tk
import json
from tkinter import ttk, messagebox


with open("data.json", "r") as f:
  global data 
  data = json.load(f)

def check_player(team, player):
  check_data_loop = True
  while check_data_loop is True:   
    #Checks if team is in data
    with open("data.json", "r") as f:
      data = json.load(f)
      if player in data["teams"][team]:
        print("data added")
        check_data_loop = False
        return True
      else:
        check_data_loop = False
        add_player(team, player)
        return True
  
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

def stat_update(statT, team, num):
  with open("data.json", "r") as f:
    data = json.load(f)
  data['teams'][team][num][statT] += 1

  with open("data.json", "w") as f:
    f.write(json.dumps(data, indent=4))

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
  messagebox.showinfo(title="Search Found", message=data["teams"][team][player][stat])

def stat_search_add_divide(team, player):
  with open("data.json", "r") as f:
    data = json.load(f)
  sumMade = data["teams"][team][player]["1"] + data["teams"][team][player]["3"]
  sumMissed = sumMade + data["teams"][team][player]["2"] + data["teams"][team][player]["4"]

  messagebox.showinfo(title="Search Found", message=str(sumMade) + "/" + str(sumMissed)) 

class game_start(tk.Toplevel):
  def __init__ (self):
    super().__init__()
    self.title("Game Start")
    self.geometry("300x300")
    self.label_home = ttk.Label(self, text="Home").pack()
    self.entry_home = ttk.Entry(self)
    self.entry_home.pack()
    self.label_away = ttk.Label(self, text="Away").pack()
    self.entry_away = ttk.Entry(self)
    self.entry_away.pack()
    self.button_start_game = ttk.Button(self, text="Start Game", command=self.create_window2)
    self.button_start_game.pack()

  def check_team(self, teamH, teamA):
    #Opens json file
    with open("data.json", "r") as f:
      data = json.load(f)
    check_data_loop = True
    #Runs until both teams are in data
    while check_data_loop is True:
      with open("data.json", "r") as f:
        data = json.load(f)
      #Checks if team is in data
      if teamH in data["teams"] and teamA in data["teams"]:
        check_data_loop = False
        return True
      elif teamH not in data["teams"] and teamA not in data["teams"]:
        check_data_loop = False
        self.add_team(teamA)
        self.add_team(teamH)
        return True
      elif teamH in data["teams"]:
        self.add_team(teamA) 
        print("added away team")
      elif teamA in data["teams"]:
        self.add_team(teamH)
        print("added home team")
      else:
        print("error 1") 
    with open("data.json", "w") as f:
      f.write(json.dumps(data, indent=4))
  
  def add_team(self, team_name):
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
      data["team num"] += 1

    with open("data.json", "w") as f:
      f.write(json.dumps(data, indent=2))
 
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
    if self.check_team(team_home_trimed, team_away_trimed) is True:
      extrawindow = choose_team()

class choose_team(tk.Toplevel):
  def __init__ (self):
    super().__init__()
    self.title("Choose Team")
    self.geometry("400x300")
    self.label_ask = ttk.Label(self, text="Choose a team").pack()
    buttonframe = ttk.Frame(self)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)

    btn1 = ttk.Button(buttonframe, text=team_home, command=self.create_window_Home)
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
    btn2 = ttk.Button(buttonframe, text=team_away, command=self.create_window_Away)
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

    buttonframe.pack(fill='x')

  def create_window_Home(self):
    extrawindow = team_frame_home()

  def create_window_Away(self):
    extrawindow = team_frame_away()

class team_frame_home(tk.Toplevel):
  def __init__ (self):
    super().__init__()
    self.title(team_home)
    self.geometry("400x300")
    self.label_num_home = ttk.Label(self, text="Enter the number and pick the stat").pack()
    self.entry_num_home = ttk.Entry(self)
    self.entry_num_home.pack()
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
      stat_update("8", team_away_trimed, self.entry_num_home.get())

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

class team_frame_away(tk.Toplevel):
  def __init__ (self):
    super().__init__()
    self.title(team_away)
    self.geometry("400x300")
    self.label_num_away = ttk.Label(self, text="Enter the number and pick the stat").pack()
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

class search_window(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("Search")
    self.geometry("300x300")
    self.label_team = ttk.Label(self, text="Team: ").pack()
    self.entry_team = ttk.Entry(self)
    self.entry_team.pack()
    self.label_num = ttk.Label(self, text="Number: ").pack()
    self.entry_num = ttk.Entry(self)
    self.entry_num.pack()
    self.button_search = ttk.Button(self, text="Search", command=self.player_search)
    self.button_search.pack()

  def player_search(self):
    global team_trimed
    team = self.entry_team.get()
    teamL = team.lower()
    team_trimed = teamL.strip()
    global ask_num
    ask_num = self.entry_num.get()
    
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

class stat_window(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("Stats")
    self.geometry("300x300")
    self.label_team = ttk.Label(self, text="What Stat do you want to look up?").pack()
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
    bnt11 = ttk.Button(buttonframe, text="Cancel Search", command=self.end_game)
    bnt11.grid(row=2, column=2, sticky=tk.W+tk.E)

    buttonframe.pack(fill="x")

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

  def end_game(self):
    self.destroy()
  
    
def create_window1():
  extrawindow = game_start()

def create_search_window():
  extrawindow = search_window()

window = tk.Tk()
window.title("Start")
window.geometry("300x300")
      
buttonframe = ttk.Frame(window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)

btn1 = ttk.Button(buttonframe, text="Start Game", command=create_window1)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = ttk.Button(buttonframe, text="Search", command=create_search_window)
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")
      
window.mainloop()