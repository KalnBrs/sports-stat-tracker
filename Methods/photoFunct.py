from Data.game import gameData
from PATH import *
from Methods.functions import *
from Methods.statObj import *
import win32com.client

pathToGraphic = getPath()
pathToBottom = getBottom()

app = win32com.client.Dispatch("Photoshop.Application")
#Opens it on the desktop For Stats
app.Open(pathToGraphic)
# Opens it for changing 
dock = app.ActiveDocument

#For actual Graphic
app.Open(pathToBottom)
# Opens it for changing 
doc1 = app.ActiveDocument


def updateBottom():
  foulPlace = doc1.ArtLayers["bottomFoulHomeNum"]
  foulPlace = foulPlace.TextItem
  if (foulPlace.Contents != str(gameData.homeFouls)):
    foulPlace.Contents = str(gameData.homeFouls)

    foulPlace.Position = (397.72414288063806, 1038.901770622075)
    if (gameData.homeFouls > 9):
      foulPlace.Position = (391.84624266889443, 1038.9029988767418)

  foulPlace = doc1.ArtLayers["bottomFoulAwayNum"]
  foulPlace = foulPlace.TextItem
  if (foulPlace.Contents != str(gameData.awayFouls)):
    foulPlace.Contents = str(gameData.awayFouls)
    foulPlace.Position = (1532.724142880638, 1037.901770622075)
    if (gameData.awayFouls > 9):
      foulPlace.Position = (1538.724142880638, 1037.901770622075)

  timePlace = doc1.ArtLayers["bottomTimeoutHomeNum"]
  timePlace = timePlace.TextItem
  if (timePlace.Contents != str(gameData.homeTimeLeft)):
    timePlace.Contents = str(gameData.homeTimeLeft)
    timePlace.Position = (651.7241428806379, 1038.901770622075)
  
  timePlace = doc1.ArtLayers["bottomTimeoutAwayNum"]
  timePlace = timePlace.TextItem
  if (timePlace.Contents != str(gameData.awayTimeLeft)):
    timePlace.Contents = str(gameData.awayTimeLeft)
    timePlace.Position = (1273.7241428806376, 1038.901770622075)

def updateTimeHome():
  gameData.homeTimeLeft -= 1

  layer1 = dock.ArtLayers["homeLeftStat"]
  layer2 = dock.ArtLayers["homeRightScore"]
  layer3 = dock.ArtLayers["homeRightStat"]
  layer1.Visible = False
  layer2.Visible = False
  layer3.Visible = False

  layer4 = dock.ArtLayers["homeLeftScore"]
  layer5 = dock.ArtLayers["homeBG"]
  layer4.Visible = True 
  layer5.Visible = True 

  timeOutLayer = dock.ArtLayers["homeLeftScore"]
  timeOutLayer = timeOutLayer.TextItem
  timeOutLayer.Contents = "TIMEOUT"

  timeOutLayer.Size = 72
  timeOutLayer.Position = (571.0564902562039, 903.0732458712706)


def updateTimeAway():
  gameData.awayTimeLeft -= 1
  TOleft = gameData.awayTimeLeft
  
  layer1 = dock.ArtLayers["awayLeftStat"]
  layer2 = dock.ArtLayers["awayRightScore"]
  layer3 = dock.ArtLayers["awayRightStat"]
  layer1.Visible = False
  layer2.Visible = False
  layer3.Visible = False

  layer4 = dock.ArtLayers["awayLeftScore"]
  layer5 = dock.ArtLayers["awayBG"]
  layer4.Visible = True 
  layer5.Visible = True 

  timeOutLayer = dock.ArtLayers["awayLeftScore"]
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
  text_layer_stat = dock.ArtLayers[layerName]
  text_layer_stat = text_layer_stat.TextItem
  text_layer_stat.Contents = statLeft
  text_layer_stat.Size = 50

  layerName = "homeLeftStat"
  text_layer_text = dock.ArtLayers[layerName]
  text_layer_text = text_layer_text.TextItem
  text_layer_text.Contents = statLeftText 
  firstPos = 378.0564902562039
  secondPos = 463.0086854673061
  if (len(statLeft) == 1):
    text_layer_stat.Position = (firstPos+10, 895.0732458712706)
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
    text_layer_stat.Position = (firstPos+40, 895.0732458712706)
    text_layer_text.Position = (secondPos+55, 895.0960563801272)
  elif (len(statLeft) == 5):
    text_layer_stat.Position = (firstPos+26, 895.0732458712706)
    text_layer_text.Position = (secondPos+50, 895.0960563801272)

  statRight = str(Home.getValueOfStat(dataOptions["statPick"][graphicRight]))
  statRightText = graphicRight
  layerName = "homeRightScore"
  text_layer_stat = dock.ArtLayers[layerName]
  text_layer_stat = text_layer_stat.TextItem
  text_layer_stat.Contents = statRight

  layerName = "homeRightStat"
  text_layer_text = dock.ArtLayers[layerName]
  text_layer_text = text_layer_text.TextItem
  text_layer_text.Contents = statRightText
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
    text_layer_stat.Position = (firstPos+20, 895.0732458712706)
    text_layer_text.Position = (secondPos+40, 895.0960563801272)
  elif (len(statRight) == 5):
    text_layer_stat.Position = (firstPos+26, 895.0732458712706)
    text_layer_text.Position = (secondPos+50, 895.0960563801272)

def shipAway(graphicLeft, graphicRight):
  showAway()
  Away = Stats("away")
  dataOptions = loadOptions()
  statLeft = str(Away.getValueOfStat(dataOptions["statPick"][graphicLeft]))
  statLeftText = graphicLeft 
  
  layerName = "awayLeftScore"
  text_layer_stat = dock.ArtLayers[layerName]
  text_layer_stat = text_layer_stat.TextItem
  text_layer_stat.Contents = statLeft
  text_layer_stat.Size = 50

  layerName = "awayLeftStat"
  text_layer_text = dock.ArtLayers[layerName]
  text_layer_text = text_layer_text.TextItem
  text_layer_text.Contents = statLeftText
  firstPos = 1149.056490256204
  secondPos = 1234.0086854673061
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
    text_layer_stat.Position = (firstPos+20, 895.0732458712706)
    text_layer_text.Position = (secondPos+40, 895.0960563801272)
  elif (len(statLeft) == 5):
    text_layer_stat.Position = (firstPos+26, 895.0732458712706)
    text_layer_text.Position = (secondPos+50, 895.0960563801272)

  statRight = str(Away.getValueOfStat(dataOptions["statPick"][graphicRight]))
  statRightText = graphicRight
  
  layerName = "awayRightScore"
  text_layer_stat = dock.ArtLayers[layerName]
  text_layer_stat = text_layer_stat.TextItem
  text_layer_stat.Contents = statRight

  layerName = "awayRightStat"
  text_layer_text = dock.ArtLayers[layerName]
  text_layer_text = text_layer_text.TextItem
  text_layer_text.Contents = statRightText
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
    text_layer_stat.Position = (firstPos+20, 895.0732458712706)
    text_layer_text.Position = (secondPos+40, 895.0960563801272)
  elif (len(statRight) == 5):
    text_layer_stat.Position = (firstPos+26, 895.0732458712706)
    text_layer_text.Position = (secondPos+50, 895.0960563801272)


def hideHome():
  layer1 = dock.ArtLayers["homeLeftScore"]
  layer2 = dock.ArtLayers["homeLeftStat"]
  layer3 = dock.ArtLayers["homeRightScore"]
  layer4 = dock.ArtLayers["homeRightStat"]
  layer5 = dock.ArtLayers["homeBG"]

  layer1.Visible = False
  layer2.Visible = False
  layer3.Visible = False
  layer4.Visible = False
  layer5.Visible = False

def hideAway():
  layer1 = dock.ArtLayers["awayLeftScore"]
  layer2 = dock.ArtLayers["awayLeftStat"]
  layer3 = dock.ArtLayers["awayRightScore"]
  layer4 = dock.ArtLayers["awayRightStat"]
  layer5 = dock.ArtLayers["awayBG"]

  layer1.Visible = False
  layer2.Visible = False
  layer3.Visible = False
  layer4.Visible = False
  layer5.Visible = False

def showHome():
  layer1 = dock.ArtLayers["homeLeftScore"]
  layer2 = dock.ArtLayers["homeLeftStat"]
  layer3 = dock.ArtLayers["homeRightScore"]
  layer4 = dock.ArtLayers["homeRightStat"]
  layer5 = dock.ArtLayers["homeBG"]

  layer1.Visible = True
  layer2.Visible = True
  layer3.Visible = True
  layer4.Visible = True
  layer5.Visible = True

def showAway():
  layer1 = dock.ArtLayers["awayLeftScore"]
  layer2 = dock.ArtLayers["awayLeftStat"]
  layer3 = dock.ArtLayers["awayRightScore"]
  layer4 = dock.ArtLayers["awayRightStat"]
  layer5 = dock.ArtLayers["awayBG"]

  layer1.Visible = True
  layer2.Visible = True
  layer3.Visible = True
  layer4.Visible = True
  layer5.Visible = True
dock.Save()
doc1.Save()