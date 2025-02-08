import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox
import ttkbootstrap as ttk
from collections import deque

#Function to use for Procedure
"""
Checks if player is in data and loops until the player is in the data 

params:
  str team: the team the player is in
  str player: the player that is going to be checked but has to be a numebr in the string

return:
  boolean: Say that the player is in the data
"""
def check_player(team, player):
  if player is not None and player.isdigit():
    check_data_loop = True
    while check_data_loop is True:   
      data = loadData()
      if player in data["teams"][team]:
        check_data_loop = False
        return True
      else:
        add_player(team, player)

  else:
    messagebox.showerror(title="Error", message="Please enter a valid number")

"""
adds the player to the data with a preset template

param:
  str team: the team the player is getting added to 
  str player: the player that is gettting added
"""
def add_player(team, player):
  my_player = {
    player: {
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

  data = loadData()
  data["teams"][team].update(my_player)

  with open("Data/data.json", "w") as f:
    json.dump(data, f, indent=2)

"""
Updates the stat by 1

param:
  str statT: The stat that is getting updated
  str team: The team that is getting updated
  str player: The player that is getting updated 
"""
def stat_update(statT, team, player):
  data = loadData()
  data['teams'][team][player][statT] += 1

  with open("Data/data.json", "w") as f:
    f.write(json.dumps(data, indent=4))

"""
Updates the points and the stats

param:
  str statT: The stat that is getting updated
  int points: How many points that are getting added 
  str team: The team that the player is apart of
  str player: The player that the stats are getting added to
"""
def stat_points_update(statT, points, team, player):
  data = loadData()
  data["teams"][team][player][statT] += 1
  data["teams"][team][player]["12"] += points

  with open("Data/data.json", "w") as f:
    f.write(json.dumps(data, indent=4))

"""
Shows the stats for Made/Total 

param:
  str team: The team that the player is a partof 
  str player: The player that you are searching
  str num1: The made stat in the data
  str num2: The missed stat in the data
"""
def stat_search_divide(team, player, num1, num2):
  data = loadData()
  messagebox.showinfo(title="Search Found", message=str(data["teams"][team][player][num1]) + "/" + str(data["teams"][team][player][num2] + data["teams"][team][player][num1]))

"""
Shows the stat for single stats

param:
  str team: The team for the player
  str player: The player that you are searching for the stat
  str stat: The stat that is getting searched for 
"""
def stat_search_add(team, player, stat):
  data = loadData()
  if data["teams"][team][player][stat] != 0:
    messagebox.showinfo(title="Search Found", message=data["teams"][team][player][stat])
  elif data["teams"][team][player][stat] == 0:
    messagebox.showinfo(title="Search Found", message="0")
  else:
    messagebox.showerror(title="Error", message="Error")

"""
Gets the Made/Total for the Threes and Twos combined 

param:
  str team: The team the player is on
  str player: The player that is getting searched for 
"""
def stat_search_add_divide(team, player):
  data = loadData()
  sumMade = data["teams"][team][player]["1"] + data["teams"][team][player]["3"]
  sumMissed = sumMade + data["teams"][team][player]["2"] + data["teams"][team][player]["4"]

  messagebox.showinfo(title="Search Found", message=str(sumMade) + "/" + str(sumMissed)) 


""" 
Shows the stats for the whole team

param:
  str team: The team that is getting searched for
"""
def replace_stats(team):
  data = loadData()

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

"""
Shows all the stats for one player

param:
  str team: The team that the player is on
  str player: The player that we are searching for 
"""
def stats_all_player(team, player):
  data = loadData()

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

"""
Checks if a single team is in the data and loops until it is added

param:
  str team: The team that is getting checked
"""
def check_team_one(team):
  check_data_loop = True
  while check_data_loop is True:
    data = loadData()
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

"""
Checks if two teams are in the data and keeps looping until they are added

param:
  str teamH: The home team that is getting checked 
  str teamA: The away team that is getting checked
"""
def check_team_two(teamH, teamA):
  data = loadData()
  check_data_loop = True
  while check_data_loop is True:
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
    elif teamA in data["teams"]:
      add_team(teamH)
    else:
      print("error 1") 
  with open("Data/data.json", "w") as f:
    f.write(json.dumps(data, indent=4))

#Adds a team into the data
"""
Adds a team into the data 

params:
  str team_name: The name of the team that is getting added 
"""
def add_team(team_name):
  num = "1"
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
  data = loadData()
  data["teams"].update(my_team)

  with open("Data/data.json", "w") as f:
    f.write(json.dumps(data, indent=2))

"""
Adds a color to the options json file and asigns it a value

param:
  str color: The color name 
  str colorValue: The hexadecimal value for that color
"""
def add_color(color, colorValue):
  optionsList = loadOptions()

  optionsList[options].append(color, 0)
  optionsList[options][color] = colorValue

  with open("Data/options.json", "w") as f:
    f.write(json.dumps(optionsList, indent=2))

"""
Gets the color value for the selected color

param:
  str color: The color that the value is going to be returned

return:
  str: The value that is put into the UI
"""
def change_color(color) -> str:
  colors = loadOptions()

  if color in colors["color-values"]:
    return colors["color-values"][color]
  else:
    return color

"""
Loads the data through open read

return:
  Object: The hashmap or json file of data
"""
def loadData():
  with open (r"Data\data.json", "r") as f:
    return json.load(f)

"""
Loads the data for the options through open read

return:
  Object: The hashmap or json file of data
"""
def loadOptions():
  with open (r"Data\options.json", "r") as f:
    return json.load(f)