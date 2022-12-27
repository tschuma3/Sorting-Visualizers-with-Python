"""
Credit: https://www.geeksforgeeks.org/visualizing-bubble-sort-using-tkinter-in-python/?ref=rp
-- Used for the visualizer aspect
"""

import time
import numpy as np
from tkinter import *
from tkinter import ttk

#Initialize root class for Tkinter
root = Tk()
root.title("Sort Visualizer")

#Maximum window size
root.maxsize(900, 600)
root.config(bg="Black")
select_Alg = StringVar()
data = []

#Bubble Sort
def bubble_Sort(data, draw_Data, timer):

    #Iterates through the data
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):

            #When j is greater than j + 1, swap
            if data[j] > data [j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

                #When swapped then display green, otherwise red
                draw_Data(data, ['Green' if x == j + 1 else 'Red' for x in range(len(data))])
                time.sleep(timer)

    #Generates green color when lines are sorted
    draw_Data(data, ['Green' for x in range(len(data))])

#Generates the values
def generate_Values():
    global data

    #Min value range
    min_Val = int(min_Entry.get())

    #Max value range
    max_Val = int(max_Entry.get())

    #Size of values
    size_Val = int(size_Entry.get())

    #Creating a blank list for data
    data = []
    for _ in range(size_Val):
        data.append(np.random.randint(min_Val, max_Val + 1))
    
    draw_Data(data, ['Red' for x in range(len(data))])

#Creating the canvas and bars
def draw_Data(data, color_List):
    canvas.delete("all")
    can_Height = 380
    can_Width = 550
    x_Width = can_Width / len(data) + 1
    offset = 30
    spacing = 10

    #Normalize data for rescalling real-valued numeric data within a given range
    normalized_Data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_Data):

        #Top left corner
        x0 = i * x_Width + offset + spacing
        y0 = can_Height - height * 340

        #Bottom right corner
        x1 = ((i + 1) * x_Width) + offset
        y1 = can_Height

        #Data bars are generated as Red colored vertical rectangles
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_List[i])
        canvas.create_text(x0 + 2, y0, anchor=SE, text=str(data[i]))
    root.update_idletasks()

#Function that initiates the sorting process
def start_Algorithm():
    global data
    bubble_Sort(data, draw_Data, speedbar.get())

#Creating the UI
#The window
window = Frame(root, width=600, height=200, bg="Grey")
window.grid(row=0, column=0, padx=10, pady=5)

#The canvas
canvas = Canvas(root, width=600, height=380, bg="Grey")
canvas.grid(row=1, column=0, padx=10, pady=5)

#Creating a user interface in grid manner
#First row components
Label(window, text="Algorithm", bg="Grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)

#Algorithm to show the name of the sorting algorithm
alg_Menu = ttk.Combobox(window, textvariable=select_Alg, values=["Bubble Sort"])
alg_Menu.grid(row=0, column=1, padx=5, pady=5)
alg_Menu.current(0)

#Creating the start button
Button(window, text="Start", bg="Blue", command=start_Algorithm).grid(row=1, column=3, padx=5, pady=5)

#Creating the speed bar using scale
speedbar = Scale(window, from_=0.10, to=2.0, length=100, digits=2,
 resolution=0.2, orient=HORIZONTAL, label="Select Speed")
speedbar.grid(row=0, column=2, padx=5, pady=5)

#Second row components
#size_Entry: scale to select the size of the data bars
size_Entry = Scale(window, from_=3, to=75, resolution=1,
                  orient=HORIZONTAL, label="Size")
size_Entry.grid(row=1, column=0, padx=5, pady=5)
 
# min_Entry : scale to select the minimum value of data bars
min_Entry = Scale(window, from_=0, to=10, resolution=1,
                 orient=HORIZONTAL, label="Minimum Value")
min_Entry.grid(row=1, column=1, padx=5, pady=5)
 
# max_Entry : scale to select the maximum value of data bars
max_Entry = Scale(window, from_=10, to=250, resolution=1,
                 orient=HORIZONTAL, label="Maximum Value")
max_Entry.grid(row=1, column=2, padx=5, pady=5)

#Creating the generate button
Button(window, text="Generate", bg="Red", command=generate_Values).grid(row=0, column=3, padx=5, pady=5)

#Stopping the main loop
root.mainloop()