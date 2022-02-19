from remDublLines import *
import tkinter as tk
from config import HEIGHT, WIDTH, SCALING


def zoomer(event):
    if (event.delta > 0):
        canvas.scale("all", event.x, event.y, 1.1, 1.1)
        # fontSize = fontSize * 1.1
    elif (event.delta < 0):
        canvas.scale("all", event.x, event.y, 0.9, 0.9)
        # fontSize = fontSize * 0.9
    canvas.configure(scrollregion=canvas.bbox("all"))
    # for child_widget in canvas.find_withtag("text"):
    #     canvas.itemconfigure(child_widget, font=("Helvetica", int(fontSize)))
    # print(fontSize)


def zoomerP(event):
    canvas.scale("all", event.x, event.y, 1.1, 1.1)
    canvas.configure(scrollregion=canvas.bbox("all"))


def zoomerM(event):
    canvas.scale("all", event.x, event.y, 0.9, 0.9)
    canvas.configure(scrollregion=canvas.bbox("all"))


def move_start(event):
    canvas.scan_mark(event.x, event.y)


def move_move(event):
    canvas.scan_dragto(event.x, event.y, gain=1)

    # move


def pressed2(event):
    global pressed
    pressed = not pressed
    canvas.scan_mark(event.x, event.y)


def move_move2(event):
    if pressed:
        canvas.scan_dragto(event.x, event.y, gain=1)


root = tk.Tk()
pressed = False


frame = tk.Frame(root, width=WIDTH / SCALING, height=HEIGHT / SCALING)
frame.pack(expand=True, fill='both')  # .grid(row=0,column=0)

canvas = tk.Canvas(frame, width=WIDTH / 50, height=HEIGHT /
                   SCALING, scrollregion=(0, 0, 30000 / 40, 40000 / 40))

xsb = tk.Scrollbar(frame, orient="horizontal")
xsb.pack(side='bottom', fill='x')
xsb.config(command=canvas.xview)

ysb = tk.Scrollbar(frame, orient="vertical")
ysb.pack(side='right', fill='y')
ysb.config(command=canvas.yview)

canvas.config(yscrollcommand=ysb.set, xscrollcommand=xsb.set)
canvas.pack(side='left', expand=True, fill='both')

# This is what enables using the mouse:
canvas.bind("<ButtonPress-1>", move_start)
canvas.bind("<B1-Motion>", move_move)

canvas.bind("<ButtonPress-2>", pressed2)
canvas.bind("<Motion>", move_move2)

# linux scroll
canvas.bind("<Button-4>", zoomerP)
canvas.bind("<Button-5>", zoomerM)
# windows scroll
canvas.bind("<MouseWheel>", zoomer)
# Hack to make zoom work on Windows
root.bind_all("<MouseWheel>", zoomer)


polygon = []
for i in range(len(idPoints) - 1):
    # Lines
    if(idPoints[i][0] == idPoints[i + 1][0] and idPoints[i][0] < 7125):
        canvas.create_line(
            idPoints[i][2] / SCALING, HEIGHT / SCALING - idPoints[i][3] /
            SCALING, idPoints[i + 1][2] / SCALING, HEIGHT /
            SCALING - idPoints[i + 1][3] / SCALING,
            fill='red')

    # Polygons
    elif(idPoints[i][0] > 7185):
        if(idPoints[i][0] != idPoints[i - 1][0] and len(polygon) > 0):
            canvas.create_polygon(
                polygon)
            polygon.clear()
        polygon.append(idPoints[i][2])
        polygon.append(HEIGHT / SCALING - idPoints[i][3])


if(__name__ == '__main__'):
    root.mainloop()
