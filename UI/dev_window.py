import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox
import ttkbootstrap as ttk
from collections import deque
from Data.game import gameData
from Methods.functions import *

class dev_window(tk.Toplevel):
  def __init__(self)
    super().__init__()
    self.title("Dev")
    self.geometry("300x300")
    self.minsize(200, 200)

    
