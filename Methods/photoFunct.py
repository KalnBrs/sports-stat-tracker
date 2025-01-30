from Data.game import gameData
import json
import math
from Methods.functions import loadData
from Methods.statObj import *

def updateTimeHome():
  print("TO Shiped")
  gameData.homeTimeLeft -= 1

def updateTimeAway():
  print("TO Shiped")
  gameData.awayTimeLeft -= 1

# Send data to photoshop
def shipHome(graphicLeft, graphicRight):
  print(graphicLeft, graphicRight)
  print("Shipped")

def shipAway(graphicLeft, graphicRight):
  print(graphicLeft, graphicRight)
  print("Shipped")
