from openpyxl import load_workbook
import openpyxl
import tkinter as tk
from tkinter import *
from os.path import dirname, abspath
import os.path
import string
import random

def randomString(stringLength=4):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def export_save(export):
    name=randomString()
    parent=dirname(dirname(abspath(__file__)))
    path = parent + '/export/' + name + '.xlsx' 
    export['file'].save(path)
    return name