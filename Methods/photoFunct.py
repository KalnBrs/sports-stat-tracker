from Data.game import gameData
import json
import math
from Methods.functions import *
from Methods.statObj import *
import win32com.client

pathToGraphic = r"C:\Users\monon\OneDrive\Desktop\Basketball\Boys\vs Oregon 010925\SCOREBOX.psd"

app = win32com.client.Dispatch("Photoshop.Application")
#Opens it on the desktop
app.Open(pathToGraphic)

# Opens it for changing 
doc = app.ActiveDocument

def updateTimeHome():
  gameData.homeTimeLeft -= 1
  TOleft = gameData.homeTimeLeft

  layer1 = doc.ArtLayers["homeLeftStat"]
  layer2 = doc.ArtLayers["homeRightScore"]
  layer3 = doc.ArtLayers["homeRightStat"]
  layer1.Visible = False
  layer2.Visible = False
  layer3.Visible = False

  layer4 = doc.ArtLayers["homeLeftScore"]
  layer5 = doc.ArtLayers["homeBG"]
  layer4.Visible = True 
  layer5.Visible = True 

  timeOutLayer = doc.ArtLayers["homeLeftScore"]
  timeOutLayer = timeOutLayer.TextItem
  timeOutLayer.Contents = "TIMEOUT"

  timeOutLayer.Size = 72
  timeOutLayer.Position = (571.0564902562039, 903.0732458712706)


def updateTimeAway():
  gameData.awayTimeLeft -= 1
  TOleft = gameData.awayTimeLeft
  
  layer1 = doc.ArtLayers["awayLeftStat"]
  layer2 = doc.ArtLayers["awayRightScore"]
  layer3 = doc.ArtLayers["awayRightStat"]
  layer1.Visible = False
  layer2.Visible = False
  layer3.Visible = False

  layer4 = doc.ArtLayers["awayLeftScore"]
  layer5 = doc.ArtLayers["awayBG"]
  layer4.Visible = True 
  layer5.Visible = True 

  timeOutLayer = doc.ArtLayers["awayLeftScore"]
  timeOutLayer = timeOutLayer.TextItem
  timeOutLayer.Contents = "TIMEOUT"

  timeOutLayer.Size = 72
  timeOutLayer.Position = (1330.0564902562044, 901.0732458712706)

# Send data to photoshop
def shipHome(graphicLeft, graphicRight):
  showHome()
  Home = Stats("home")
  dataOptions = loadOptions()
  statLeft = str(Home.getValueOfStat(dataOptions["statPick"][graphicLeft]))
  statLeftText = graphicLeft 

  layerName = "homeLeftScore"
  text_layer_stat = doc.ArtLayers[layerName]
  text_layer_stat = text_layer_stat.TextItem
  text_layer_stat.Contents = statLeft
  text_layer_stat.Size = 50

  layerName = "homeLeftStat"
  text_layer_text = doc.ArtLayers[layerName]
  text_layer_text = text_layer_text.TextItem
  text_layer_text.Contents = statLeftText
  print(f"Left text{text_layer_stat.Position}")
  print(f"Left stat{text_layer_text.Position}")  
  firstPos = 378.0564902562039
  secondPos = 463.0086854673061
  if (len(statLeft) == 1):
    text_layer_stat.Position = (firstPos, 895.0732458712706)
    text_layer_text.Position = (secondPos, 895.0960563801272)
  elif (len(statLeft) == 2 and len(statLeftText) != 4):
    text_layer_stat.Position = (firstPos+2, 895.0732458712706)
    text_layer_text.Position = (secondPos+12, 895.0960563801272)
  elif (len(statLeft) == 2 and len(statLeftText) == 4):
    text_layer_stat.Position = (firstPos+46, 895.0732458712706)
    text_layer_text.Position = (secondPos+20, 895.0960563801272)
  elif (len(statLeft) == 3):
    text_layer_stat.Position = (firstPos+32, 895.0732458712706)
    text_layer_text.Position = (secondPos+35, 895.0960563801272)
  elif (len(statLeft) == 4):
    text_layer_stat.Position = (firstPos-2, 895.0732458712706)
    text_layer_text.Position = (secondPos+10, 895.0960563801272)
  elif (len(statLeft) == 5):
    text_layer_stat.Position = (firstPos+26, 895.0732458712706)
    text_layer_text.Position = (secondPos+50, 895.0960563801272)

  statRight = str(Home.getValueOfStat(dataOptions["statPick"][graphicRight]))
  statRightText = graphicRight
  layerName = "homeRightScore"
  text_layer_stat = doc.ArtLayers[layerName]
  text_layer_stat = text_layer_stat.TextItem
  text_layer_stat.Contents = statRight

  layerName = "homeRightStat"
  text_layer_text = doc.ArtLayers[layerName]
  text_layer_text = text_layer_text.TextItem
  text_layer_text.Contents = statRightText
  print(f"Right text{text_layer_stat.Position}")
  print(f"Righ stat{text_layer_text.Position}")
  firstPos = 597.0555500271992
  secondPos = 677.0077828293704
  if (len(statRight) == 1):
    text_layer_stat.Position = (firstPos, 895.0732458712706)
    text_layer_text.Position = (secondPos, 895.0960563801272)
  elif (len(statRight) == 2 and len(statRightText) != 4):
    text_layer_stat.Position = (firstPos-8, 895.0732458712706)
    text_layer_text.Position = (secondPos+12, 895.0960563801272)
  elif (len(statRight) == 2 and len(statRightText) == 4):
    text_layer_stat.Position = (firstPos+46, 895.0732458712706)
    text_layer_text.Position = (secondPos+20, 895.0960563801272)
  elif (len(statRight) == 3):
    text_layer_stat.Position = (firstPos+32, 895.0732458712706)
    text_layer_text.Position = (secondPos+35, 895.0960563801272)
  elif (len(statRight) == 4):
    text_layer_stat.Position = (firstPos-2, 895.0732458712706)
    text_layer_text.Position = (secondPos+10, 895.0960563801272)
  elif (len(statRight) == 5):
    text_layer_stat.Position = (firstPos+26, 895.0732458712706)
    text_layer_text.Position = (secondPos+50, 895.0960563801272)
  

  print(f"{statLeft} - {statLeftText} {statRight} - {statRightText}")

def shipAway(graphicLeft, graphicRight):
  showAway()
  Away = Stats("away")
  dataOptions = loadOptions()
  statLeft = str(Away.getValueOfStat(dataOptions["statPick"][graphicLeft]))
  statLeftText = graphicLeft 
  
  layerName = "awayLeftScore"
  text_layer_stat = doc.ArtLayers[layerName]
  text_layer_stat = text_layer_stat.TextItem
  text_layer_stat.Contents = statLeft
  text_layer_stat.Size = 50

  layerName = "awayLeftStat"
  text_layer_text = doc.ArtLayers[layerName]
  text_layer_text = text_layer_text.TextItem
  text_layer_text.Contents = statLeftText
  print(f"Left text{text_layer_stat.Position}")
  print(f"Left stat{text_layer_text.Position}") 
  firstPos = 1139.056490256204
  secondPos = 1224.0086854673061
  if (len(statLeft) == 1):
    text_layer_stat.Position = (firstPos, 895.0732458712706)
    text_layer_text.Position = (secondPos, 895.0960563801272)
  elif (len(statLeft) == 2 and len(statLeftText) != 4):
    text_layer_stat.Position = (firstPos+2, 895.0732458712706)
    text_layer_text.Position = (secondPos+12, 895.0960563801272)
  elif (len(statLeft) == 2 and len(statLeftText) == 4):
    text_layer_stat.Position = (firstPos+46, 895.0732458712706)
    text_layer_text.Position = (secondPos+20, 895.0960563801272)
  elif (len(statLeft) == 3):
    text_layer_stat.Position = (firstPos+32, 895.0732458712706)
    text_layer_text.Position = (secondPos+35, 895.0960563801272)
  elif (len(statLeft) == 4):
    text_layer_stat.Position = (firstPos-2, 895.0732458712706)
    text_layer_text.Position = (secondPos+10, 895.0960563801272)
  elif (len(statLeft) == 5):
    text_layer_stat.Position = (firstPos+26, 895.0732458712706)
    text_layer_text.Position = (secondPos+50, 895.0960563801272)

  statRight = str(Away.getValueOfStat(dataOptions["statPick"][graphicRight]))
  statRightText = graphicRight
  
  layerName = "awayRightScore"
  text_layer_stat = doc.ArtLayers[layerName]
  text_layer_stat = text_layer_stat.TextItem
  text_layer_stat.Contents = statRight

  layerName = "awayRightStat"
  text_layer_text = doc.ArtLayers[layerName]
  text_layer_text = text_layer_text.TextItem
  text_layer_text.Contents = statRightText
  print(f"Right text{text_layer_stat.Position}")
  print(f"Righ stat{text_layer_text.Position}")
  firstPos = 1357.0555500271992
  secondPos = 1438.0077828293704
  if (len(statRight) == 1):
    text_layer_stat.Position = (firstPos, 895.0732458712706)
    text_layer_text.Position = (secondPos, 895.0960563801272)
  elif (len(statRight) == 2 and len(statRightText) != 4):
    text_layer_stat.Position = (firstPos-8, 895.0732458712706)
    text_layer_text.Position = (secondPos+12, 895.0960563801272)
  elif (len(statRight) == 2 and len(statRightText) == 4):
    text_layer_stat.Position = (firstPos+46, 895.0732458712706)
    text_layer_text.Position = (secondPos+20, 895.0960563801272)
  elif (len(statRight) == 3):
    text_layer_stat.Position = (firstPos+32, 895.0732458712706)
    text_layer_text.Position = (secondPos+35, 895.0960563801272)
  elif (len(statRight) == 4):
    text_layer_stat.Position = (firstPos-2, 895.0732458712706)
    text_layer_text.Position = (secondPos+10, 895.0960563801272)
  elif (len(statRight) == 5):
    text_layer_stat.Position = (firstPos+26, 895.0732458712706)
    text_layer_text.Position = (secondPos+50, 895.0960563801272)

  print(f"{statLeft} - {statLeftText} {statRight} - {statRightText}")

def hideHome():
  layer1 = doc.ArtLayers["homeLeftScore"]
  layer2 = doc.ArtLayers["homeLeftStat"]
  layer3 = doc.ArtLayers["homeRightScore"]
  layer4 = doc.ArtLayers["homeRightStat"]
  layer5 = doc.ArtLayers["homeBG"]

  layer1.Visible = False
  layer2.Visible = False
  layer3.Visible = False
  layer4.Visible = False
  layer5.Visible = False

def hideAway():
  layer1 = doc.ArtLayers["awayLeftScore"]
  layer2 = doc.ArtLayers["awayLeftStat"]
  layer3 = doc.ArtLayers["awayRightScore"]
  layer4 = doc.ArtLayers["awayRightStat"]
  layer5 = doc.ArtLayers["awayBG"]

  layer1.Visible = False
  layer2.Visible = False
  layer3.Visible = False
  layer4.Visible = False
  layer5.Visible = False

def showHome():
  layer1 = doc.ArtLayers["homeLeftScore"]
  layer2 = doc.ArtLayers["homeLeftStat"]
  layer3 = doc.ArtLayers["homeRightScore"]
  layer4 = doc.ArtLayers["homeRightStat"]
  layer5 = doc.ArtLayers["homeBG"]

  layer1.Visible = True
  layer2.Visible = True
  layer3.Visible = True
  layer4.Visible = True
  layer5.Visible = True

def showAway():
  layer1 = doc.ArtLayers["awayLeftScore"]
  layer2 = doc.ArtLayers["awayLeftStat"]
  layer3 = doc.ArtLayers["awayRightScore"]
  layer4 = doc.ArtLayers["awayRightStat"]
  layer5 = doc.ArtLayers["awayBG"]

  layer1.Visible = True
  layer2.Visible = True
  layer3.Visible = True
  layer4.Visible = True
  layer5.Visible = True
doc.Save()