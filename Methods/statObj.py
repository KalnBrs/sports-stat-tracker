from Data.game import gameData
import json
import math
from Methods.functions import loadData

class Stats():
  def __init__(self, team):
    self.team = team
    self.trimed = ""
    self.gameTimeout = None

    if self.team == "home":
      self.trimed = gameData.team_home_trimed
    elif self.team == "away":
      self.trimed = gameData.team_away_trimed

  def restOfStats(self, statID):
    data = loadData()

    if statID == 13:
      return data["teams"][self.trimed]["1"]["5"]
    if statID == 14:
      return data["teams"][self.trimed]["1"]["6"]
    if statID == 15:
      return data["teams"][self.trimed]["1"]["7"]
    if statID == 16:
      return data["teams"][self.trimed]["1"]["8"]
    if statID == 17:
      return data["teams"][self.trimed]["1"]["9"]
    if statID == 18:
      if self.team == "home":
        self.gameTimeout = gameData.homeTimeLeft
      elif self.team == "away":
        self.gameTimeout = gameData.awayTimeLeft
      return self.gameTimeout
    if statID == 19:
      if self.team == "home":
        return gameData.homeFouls
      return gameData.awayFouls

  def getFT(self, statID):
    data = loadData()

    if statID == 9:
      return data["teams"][self.trimed]["1"]["10"]
    if statID == 10:
      return data["teams"][self.trimed]["1"]["11"]
    if statID == 11:
      try:
        return str(math.trunc((self.getFT(9) / (self.getFT(10) + self.getFT(9))) * 100))
      except:
        return "0"
    if statID == 12:
      return str(self.getFT(9)) + "/" + str(self.getFT(10) + self.getFT(9))

  def getThree(self, statID):
    data = loadData()

    if statID == 5:
      return data["teams"][self.trimed]["1"]["3"]
    if statID == 6:
      return data["teams"][self.trimed]["1"]["4"]
    if statID == 7:
      try:
        return str(math.trunc((self.getThree(5) / (self.getThree(6) + self.getThree(5))) * 100))
      except:
        return "0"
    if statID == 8:
      return str(self.getThree(5)) + "/" + str(self.getThree(6) + self.getThree(5))

  def getFieldGoal(self, statID):
    data = loadData()

    if statID == 1:
      return data["teams"][self.trimed]["1"]["1"] + data["teams"][self.trimed]["1"]["3"]
    if statID == 2:
      return data["teams"][self.trimed]["1"]["2"] + data["teams"][self.trimed]["1"]["4"]
    if statID == 3:
      try:
        return str(math.trunc((self.getFieldGoal(1) / (self.getFieldGoal(2) + self.getFieldGoal(1))) * 100))
      except:
        return "0"
    if statID == 4:
      return str(self.getFieldGoal(1)) + "/" + str(self.getFieldGoal(2) + self.getFieldGoal(1))

  def getValueOfStat(self, statID):
    data = loadData()

    if statID == 0:
      return "None"
    if statID > 0 and statID < 5:
      return self.getFieldGoal(statID)
    if statID > 4 and statID < 9:
      return self.getThree(statID)
    if statID > 8 and statID < 13:
      return self.getFT(statID)
    else:
      return self.restOfStats(statID)