# This class contains the data needed for the program
class gameData():
  def __init__(self):
    self.team_home = ""
    self.team_home_trimed = ""
    self.team_away = ""
    self.team_away_trimed = ""
    self.homeColor = ""
    self.awayColor = ""
    self.homeTimeLeft = 5
    self.awayTimeLeft = 5
    self.homeFouls = 0
    self.awayFouls = 0

  def getHome():
    return self.team_home

  def getHomeTrimmed():
    return self.team_home_trimed

  def getAway():
    return self.team_away

  def getAwayTrimed():
    return self.team_away_trimed