from Data.game import gameData
import json
import math
from Methods.functions import *
from Methods.statObj import *

def updateTimeHome():
  gameData.homeTimeLeft -= 1
  TOleft = gameData.homeTeamLeft

def updateTimeAway():
  gameData.awayTimeLeft -= 1
  TOleft = gameData.homeTeamLeft

# Send data to photoshop
def shipHome(graphicLeft, graphicRight):
  Home = Stats("home")
  dataOptions = loadOptions()
  statLeft = str(Home.getValueOfStat(dataOptions["statPick"][graphicLeft]))
  statLeftText = graphicLeft 

  statRight = str(Home.getValueOfStat(dataOptions["statPick"][graphicRight]))
  statRightText = graphicRight

  print(f"{statLeft} - {statLeftText} {statRight} - {statRightText}")

def shipAway(graphicLeft, graphicRight):
  Away = Stats("away")
  dataOptions = loadOptions()
  statLeft = str(Away.getValueOfStat(dataOptions["statPick"][graphicLeft]))
  statLeftText = graphicLeft 

  statRight = str(Away.getValueOfStat(dataOptions["statPick"][graphicRight]))
  statRightText = graphicRight

  print(f"{statLeft} - {statLeftText} {statRight} - {statRightText}")
