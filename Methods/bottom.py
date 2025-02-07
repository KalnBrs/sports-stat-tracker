import win32com.client
from PATH import *
from Data.game import gameData

pathToBottom = getBottom()

app = win32com.client.Dispatch("Photoshop.Application")

#For actual Graphic
app.Open(pathToBottom)
# Opens it for changing 
doc1 = app.ActiveDocument

def updateBottom():
  doc1.Activate()
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
