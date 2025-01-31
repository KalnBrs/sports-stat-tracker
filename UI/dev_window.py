import tkinter as tk
from tkinter import *
import json
from ttkbootstrap.dialogs import Messagebox
import ttkbootstrap as ttk
from collections import deque
from Data.game import gameData
from Methods.functions import *

class dev_window(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("Dev")
    self.geometry("300x300")
    self.minsize(300, 300)

    addColor = ttk.Button(self, text="Add Color", command=self.addWindow)
    addColor.pack(pady=10)

    dataButton = ttk.Button(self, text="Reset Data", command=self.resetData)
    dataButton.pack()

    data = loadOptions()
    self.clicked = StringVar()
    self.clicked.set("None")

    colorLabelPick = ttk.Label(self, text="Pick a color:").pack(pady=5)
    drop = OptionMenu(self, self.clicked, *data["options"])
    drop.pack()

    colorLabelNew = ttk.Label(self, text="New Value (#000000):").pack(pady=5)
    self.colorEntry = ttk.Entry(self)
    self.colorEntry.pack()

    changeColor = ttk.Button(self, text="Change Color Value", command=self.changeColorValue)
    changeColor.pack(pady=10)

  def resetData(self):
    correctData = {"teams": {
      "team_name": {
        "player": {
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
    }}
    check = Messagebox.yesno(
      title = "Confirmation", 
      message="Are you sure you want to clear all data"
    )

    if check:
      data = loadData()
      data = correctData

      with open("Data/data.json", "w") as f:
        f.write(json.dumps(data, indent=2))
    else:
      pass

  def changeColorValue(self):
    dataOptions = loadOptions()
    code = self.colorEntry.get()
    print(code)

    if code[0] == "#" and len(code) == 7:
      print(dataOptions["color-values"])
      print(self.clicked.get())
      print(type(dataOptions["color-values"]))
      dataOptions["color-values"][self.clicked.get()] = code
      print(dataOptions["color-values"])
    else:
      Messagebox.show_error(
        title="Error",
        message="Please input a valid hex code (#000000)"
      )

    with open("Data/options.json", "w") as f:
      json.dump(dataOptions, f, indent=2)

  def addWindow(self):
    a = add_color()

class add_color(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("Add Color")
    self.geometry("300x300")
    self.minsize(300, 300)

    nameLabel = ttk.Label(self, text="Color Name:").pack()
    self.nameEntry = ttk.Entry(self)
    self.nameEntry.pack()

    valueLabel = ttk.Label(self, text="Color Value (#000000):").pack()
    self.valueEntry = ttk.Entry(self)
    self.valueEntry.pack()

    submitButton = ttk.Button(self, text="Submit", command=self.submit)
    submitButton.pack()

  def submit(self):
    dataOptions = loadOptions()
    code = self.valueEntry.get()

    if self.nameEntry.get() not in dataOptions["options"]:
      dataOptions["options"].insert(0, self.nameEntry.get())

    if code[0] == "#" and len(code) == 7:
      print(dataOptions["color-values"])
      print(self.nameEntry.get())
      print(type(dataOptions["color-values"]))
      dataOptions["color-values"][self.nameEntry.get()] = code
      print(dataOptions["color-values"])
    else:
      Messagebox.show_error(
        title="Error",
        message="Please input a valid hex code (#000000)"
      )

    with open("Data/options.json", "w") as f:
      json.dump(dataOptions, f, indent=2)
