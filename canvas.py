# from cmath import pi
import csv
from textwrap import fill
import tkinter as tk
# import random
from config import WIDTH, HEIGHT, SCALING
import time


# idPoints = []
# with open('IdPoints.csv', newline='') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         point = [float(i) for i in row[0].split(';')]
#         idPoints.append(point)

# Delete duplicate lines
from remDublLines import *

pressed = False

class Example(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(
            self, width=WIDTH / SCALING, height=HEIGHT / SCALING)
        self.xsb = tk.Scrollbar(self, orient="horizontal",
                                command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient="vertical",
                                command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set,
                              xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0, 0, 1000, 1000))

        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.fontSize = 10

        polygon = []
        for i in range(len(idPoints) - 1):
            # Lines
            if(idPoints[i][0] == idPoints[i + 1][0] and idPoints[i][0] < 7125):
                self.canvas.create_line(
                    idPoints[i][2] / SCALING, 40000 / SCALING - idPoints[i][3] /
                    SCALING, idPoints[i + 1][2] / SCALING, 40000 /
                    SCALING - idPoints[i + 1][3] / SCALING,
                    fill='red')

            # Polygons
            elif(idPoints[i][0] > 7185):
                if(idPoints[i][0] != idPoints[i - 1][0] and len(polygon) > 0):
                    self.canvas.create_polygon(
                        polygon)
                    polygon.clear()
                polygon.append(idPoints[i][2])
                polygon.append(40000 - idPoints[i][3])


        # This is what enables using the mouse:
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)

        self.canvas.bind("<ButtonPress-2>", self.pressed2)
        self.canvas.bind("<Motion>", self.move_move2)

        # linux scroll
        self.canvas.bind("<Button-4>", self.zoomerP)
        self.canvas.bind("<Button-5>", self.zoomerM)
        # windows scroll
        # self.canvas.bind("<MouseWheel>",self.zoomer)
        # Hack to make zoom work on Windows
        root.bind_all("<MouseWheel>", self.zoomer)

    # def create_road(self):

    # move

    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    # move
    def pressed2(self, event):
        global pressed
        pressed = not pressed
        self.canvas.scan_mark(event.x, event.y)

    def move_move2(self, event):
        if pressed:
            self.canvas.scan_dragto(event.x, event.y, gain=1)

    # windows zoom
    def zoomer(self, event):
        if (event.delta > 0):
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
            # self.fontSize = self.fontSize * 1.1
        elif (event.delta < 0):
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
            # self.fontSize = self.fontSize * 0.9
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        # for child_widget in self.canvas.find_withtag("text"):
        #     self.canvas.itemconfigure(child_widget, font=("Helvetica", int(self.fontSize)))
        # print(self.fontSize)

    # linux zoom
    def zoomerP(self, event):
        self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def zoomerM(self, event):
        self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
