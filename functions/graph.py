import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import *

def graph(x,y,root,P,color,label):
    
    R = [None] * len(x)
    for i in range (0,len(x)):
        R[i]=i

    P.plot(R,y,color,label=label)
    P.set_ylim([0, 125])
    P.set_xticks(R)
    P.set_xticklabels(x)
    P.tick_params(axis='x', rotation=45)
    P.grid()
    P.legend(bbox_to_anchor=(1, 1))
    root.draw()
    P.grid()
     
    