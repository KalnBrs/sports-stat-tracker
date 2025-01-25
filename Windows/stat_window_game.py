import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox
import ttkbootstrap as ttk
from collections import deque
from game import gameData
from Methods.functions import *
from Windows.photoshopDashboard import dashboard

# Updating Stat Window
class Stat_Window_Game(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("Stats")
    self.geometry("500x500")
    self.minsize(200, 350)

    self.teamHome = StringVar()
    self.teamHome.set(gameData.team_home)

    self.teamAway = StringVar()
    self.teamAway.set(gameData.team_away)

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

    self.reload = ttk.Button(self, text="Reload", command=self.set_variables).pack()

    self.dash = ttk.Button(self, text="Photoshop Dashboard", command=self.openDash).pack()

    
    self.mainloop()

  def openDash(self):
    dashWindow = dashboard()

  def set_variables(self):
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

    for x in data["teams"][gameData.team_home_trimed]:

      twoMadeHomeInt += data["teams"][gameData.team_home_trimed][x]["1"]
      twoMissedHomeInt += data["teams"][gameData.team_home_trimed][x]["2"]
      threeMadeHomeInt += data["teams"][gameData.team_home_trimed][x]["3"]
      threeMissedHomeInt += data["teams"][gameData.team_home_trimed][x]["4"]
      reboundsHomeInt += data["teams"][gameData.team_home_trimed][x]["5"]
      turnoversHomeInt += data["teams"][gameData.team_home_trimed][x]["6"]
      stealHomeInt += data["teams"][gameData.team_home_trimed][x]["7"]
      assistsHomeInt += data["teams"][gameData.team_home_trimed][x]["8"]
      blocksHomeInt += data["teams"][gameData.team_home_trimed][x]["9"]
      freeTrowsMadeHomeInt += data["teams"][gameData.team_home_trimed][x]["10"]
      freeThrowsMissedHomeInt += data["teams"][gameData.team_home_trimed][x]["11"]
      pointsHomeInt += data["teams"][gameData.team_home_trimed][x]["12"]

    for x in data["teams"][gameData.team_away_trimed]:
      twoMadeAwayInt += data["teams"][gameData.team_away_trimed][x]["1"]
      twoMissedAwayInt += data["teams"][gameData.team_away_trimed][x]["2"]
      threeMadeAwayInt += data["teams"][gameData.team_away_trimed][x]["3"]
      threeMissedAwayInt += data["teams"][gameData.team_away_trimed][x]["4"]
      reboundsAwayInt += data["teams"][gameData.team_away_trimed][x]["5"]
      turnoversAwayInt += data["teams"][gameData.team_away_trimed][x]["6"]
      stealAwayInt += data["teams"][gameData.team_away_trimed][x]["7"]
      assistsAwayInt += data["teams"][gameData.team_away_trimed][x]["8"]
      blocksAwayInt += data["teams"][gameData.team_away_trimed][x]["9"]
      freeTrowsMadeAwayInt += data["teams"][gameData.team_away_trimed][x]["10"]
      freeThrowsMissedAwayInt += data["teams"][gameData.team_away_trimed][x]["11"]
      pointsAwayInt += data["teams"][gameData.team_away_trimed][x]["12"]


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

    self.after(100, self.set_variables)

