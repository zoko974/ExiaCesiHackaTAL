#!/usr/bin/env python
# coding: utf-8
from Tkinter import *
import csv 
from tempfile import NamedTemporaryFile

import string
exclude = string.punctuation
#import networkx as nx

import Tkinter as tk
import platform


import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import sys
import os
import tkMessageBox

#tkMessageBox.showinfo(title="Greetings", message="Hello World!")





class Application(Frame):
    

    def linemaker(self,screen_points):
        """ Function to take list of points and make them into lines
        """
        is_first = True
        # Set up some variables to hold x,y coods
        x0 = y0 = 0
        # Grab each pair of points from the input list
        for (x,y) in screen_points:
            # If its the first point in a set, set x0,y0 to the values
            if is_first:
                x0 = x
                y0 = y
                is_first = False
            else:
                # If its not the fist point yeild previous pair and current pair
                yield x0,y0,x,y
                # Set current x,y to start coords of next line
                x0,y0 = x,y

    def makeentry(parent, caption, width=None, **options):
        Label(parent, text=caption).pack(side=LEFT)
        entry = Entry(parent, **options)
        if width:
            entry.config(width=width)
        entry.pack(side=LEFT)
        return entry

    def traitementAlgo(self):

        

        print(str.split(self.E1.get()))
        ListMot=str.split(self.E1.get())

        for Mot in ListMot:
            if platform.system() == "Windows":
                os.system("AffichageGraphique.py "+Mot)
            else :
                os.system("./AffichageGraphique.py "+Mot)

    def traitementAlgo2(self):

        

        print(str.split(self.E1.get()))
        ListMot=str.split(self.E1.get())

        for Mot in ListMot:
            if platform.system() == "Windows":
                os.system("AffichageGraphique2.py "+Mot)
            else :
                os.system("python AffichageGraphique2.py "+Mot)

    def traitementAlgo3(self):

        

        print(str.split(self.E1.get()))
        ListMot=str.split(self.E1.get())

        for Mot in ListMot:
            if platform.system() == "Windows":
                os.system("AffichageGraphique3.py "+Mot)
            else :
                os.system("python AffichageGraphique3.py "+Mot)



    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        L1 = Label(self, text="Entrez votre recherche")
        L1.pack( side = LEFT)
        self.E1 = Entry(self, bd =5)

        self.E1.pack(side = LEFT)

        self.traitementButton = Button(self)
        self.traitementButton["text"] = "Visualisation3D",
        self.traitementButton["command"] = self.traitementAlgo

        self.traitementButton.pack({"side": "left"})

        self.traitementButton2 = Button(self)
        self.traitementButton2["text"] = "Camembert",
        self.traitementButton2["command"] = self.traitementAlgo2

        self.traitementButton2.pack({"side": "left"})

        self.traitementButton3 = Button(self)
        self.traitementButton3["text"] = "Histogramme",
        self.traitementButton3["command"] = self.traitementAlgo3

        self.traitementButton3.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


        #with open("types.tsv") as tsvfile:
        #    tsvreader = csv.reader(tsvfile, delimiter="\t")
            
        #    for row in tsvreader:
         #       if len(row[0]) >= 4:
                    #print(row[0])
            



root = Tk()
root.title("TAL Project")

#cv = tk.Canvas(root,height="500",width="500",bg="white")
#cv.pack()



app = Application(master=root)
app.mainloop()
root.destroy()




