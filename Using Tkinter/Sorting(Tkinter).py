"""
Credit
-- https://www.geeksforgeeks.org/visualizing-bubble-sort-using-tkinter-in-python/?ref=rp
-- https://www.geeksforgeeks.org/visualizing-quick-sort-using-tkinter-in-python/?ref=rp
~ Used for the visualizer aspect
"""

import time
import numpy as np
from tkinter import *
from tkinter import ttk

#Initialize root class for Tkinter
root = Tk()
root.title("Sort Visualizer")

#Maximum window size
root.maxsize(900, 800)
root.config(bg="Black")
select_Alg = StringVar()
data = []

#region Sorting Algorithms

#region Bubble Sort
def bubble_Sort(data, draw_Data, timer):

    #Iterates through the data
    for i in range(len(data) - 1):

        #draw_Data(data, get_Color_Array_Bubble(len(data), i, i))
        #time.sleep(timer)

        for j in range(len(data) - i - 1):

            #draw_Data(data, get_Color_Array_Bubble(len(data), i, j))
            #time.sleep(timer)

            #When j is greater than j + 1, swap
            if data[j] > data [j + 1]:

                draw_Data(data, get_Color_Array_Bubble(len(data), j, j + 1))
                time.sleep(timer)

                data[j], data[j + 1] = data[j + 1], data[j]

                draw_Data(data, get_Color_Array_Bubble(len(data), j, j + 1, True))
                time.sleep(timer)

# Function to apply colors to bars while sorting:
# Grey - Searched elements
# Blue - Lowest element
# White - Unsearched elements
# Yellow - Current index
# Green - after all elements are sorted
def get_Color_Array_Bubble(data_Len, curr_Index, curr_Index_1, is_Swaping = False):
    color_Array = []
    for j in range(data_Len):
        #Base color
        if j <= curr_Index and j <= data_Len:
            color_Array.append('Grey')
        else:
            color_Array.append('White')

        if j == curr_Index:
            color_Array[j] = 'Yellow'
        elif j == curr_Index_1:
            color_Array[j] = 'Blue'
        
        if is_Swaping:
            if j == curr_Index:
                color_Array[j] = 'Green'
    
    return color_Array

#endregion

#region Quick Sort Algorithm
def quick_Sort(data, low, high, draw_Data, timer):

    if low <= high:
        #Finds the pivot
        pi = partition(data, low, high, draw_Data, timer)

        #Works the left side
        quick_Sort(data, low, pi - 1, draw_Data, timer)

        #Works the right side
        quick_Sort(data, pi + 1, high, draw_Data, timer)

def partition(data, low, high, draw_Data, timer):

    #Pointer to the greater element
    i = low

    #Sets the pivot to the last element and boarder to low
    pivot = data[high]

    #Draws the intended colors
    draw_Data(data, get_Color_Array_Quick(len(data), low, high, i, i))
    time.sleep(timer)

    #Iterates through the data and checks j to the pivot
    for j in range(low, high):
        if data[j] < pivot:

            #Draws the intended colors
            draw_Data(data, get_Color_Array_Quick(len(data), low, high, i, j, True))
            time.sleep(timer)

            #Swaps j and i
            data[j], data[i] = data[i], data[j]
            #Greater element pointer
            i += 1

        #Draws the intended colors
        draw_Data(data, get_Color_Array_Quick(len(data), low, high, i, j))
        time.sleep(timer)
    
    #Draws the intended colors
    draw_Data(data, get_Color_Array_Quick(len(data), low, high, i, high, True))
    time.sleep(timer)

    #Swaps the pivot element with the high
    data[i], data[high] = data[high], data[i]

    return i

# Function to apply colors to bars while sorting:
# Grey - Unsorted elements
# Blue - Pivot point element
# White - Sorted half/partition
# Red - Starting pointer
# Yellow - Ending pointer
# Green - after all elements are sorted
def get_Color_Array_Quick(data_Len, low, high, i, curr_Index, is_Swaping = False):
    color_Array = []
    for j in range(data_Len):
        #Base color
        if j >= low and j <= high:
            color_Array.append('Grey')
        else:
            color_Array.append('White')

        if j == low:
            color_Array[j] = 'Blue'
        elif j == i:
            color_Array[j] = 'Red'
        elif j == curr_Index:
            color_Array[j] = 'Yellow'
        
        if is_Swaping:
            if j == i or j == curr_Index:
                color_Array[j] = 'Green'
    
    return color_Array

#endregion

#region Selection Sort
def selection_Sort(data, low, high, draw_Data, timer):
    for i in range(high):
        low = i

        draw_Data(data, get_Color_Array_Selection(high, low, high, i))
        time.sleep(timer)

        for j in range(i + 1, high):
            if data[low] > data[j]:
                low = j

                draw_Data(data, get_Color_Array_Selection(high, low, high, j))
                time.sleep(timer)

        data[i], data[low] = data[low], data[i]

        draw_Data(data, get_Color_Array_Selection(high, low, high, i, True))
        time.sleep(timer)

# Function to apply colors to bars while sorting:
# Grey - Unsorted elements
# Blue - Lowest element
# White - Sorted elements
# Yellow - Current index
# Green - after all elements are sorted
def get_Color_Array_Selection(data_Len, low, high, curr_Index, is_Swaping = False):
    color_Array = []
    for j in range(data_Len):
        #Base color
        if j >= low and j <= high:
            color_Array.append('Grey')
        else:
            color_Array.append('White')

        if j == low:
            color_Array[j] = 'Blue'
        elif j == curr_Index:
            color_Array[j] = 'Yellow'
        
        if is_Swaping:
            if j == curr_Index:
                color_Array[j] = 'Green'
    
    return color_Array

#endregion

#region Heap Sort

def heap_Sort(data, draw_Data, timer):
    high = len(data)

    #Building a maxheap
    for i in range(high // 2 - 1, -1, -1):
        heapify(data, high, i, draw_Data, timer)

    #Extract the elements one by one
    for i in range(high - 1, 0, -1):
        data[i], data[0] = data[0], data[i]

        draw_Data(data, get_Color_Array_Heap(len(data), data[0], i, True))
        time.sleep(timer)

        heapify(data, i, 0)

def heapify(data, high, i, draw_Data, timer):
    
    #Initialize the largest as root
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    #Checks the left child
    if left< high and data[largest] < data[left]:
        largest = left
    
    #Checks right child
    if right < high and data[largest] < data[right]:
        largest = right
    
    #Change root, when needed
    if largest != i:

        #Swap
        data[i], data[largest] = data[largest], data[i]

        draw_Data(data, get_Color_Array_Heap(len(data), i, largest, True))
        time.sleep(timer)

        #Heapify
        heapify(data, high, largest)

# Function to apply colors to bars while sorting:
# Grey - Searched elements
# Blue - Largest element
# White - Unsearched elements
# Yellow - i index
# Green - after all elements are sorted
def get_Color_Array_Heap(data_Len, i, largest, is_Swaping = False):
    color_Array = []
    for j in range(data_Len):
        #Base color
        if j <= i and j <= data_Len:
            color_Array.append('Grey')
        else:
            color_Array.append('White')

        if j == i:
            color_Array[j] = 'Yellow'
        elif j == largest:
            color_Array[j] = 'Blue'
        
        if is_Swaping:
            if j == curr_Index:
                color_Array[j] = 'Green'
    
    return color_Array

#endregion

#endregion

#region Vizualiztion

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
    can_Height = 480
    can_Width = 727
    x_Width = can_Width / len(data) + 1
    offset = 30
    spacing = 10

    #Normalize data for rescalling real-valued numeric data within a given range
    normalized_Data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_Data):

        #Top left corner
        x0 = i * x_Width + offset + spacing
        y0 = can_Height - height * 450

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
    low = 0
    high = len(data)

    if not data:
        return

    if alg_Menu.get() == 'Bubble Sort':
        bubble_Sort(data, draw_Data, speedbar.get())
    elif alg_Menu.get() == 'Quick Sort':
        quick_Sort(data, low, high - 1, draw_Data, speedbar.get())
    elif alg_Menu.get() == 'Selection Sort':
        selection_Sort(data, low, high, draw_Data, speedbar.get())
    elif alg_Menu.get() == 'Heap Sort':
        heap_Sort(data, draw_Data, speedbar.get())

    #Color every bar green when done sorting
    draw_Data(data, ['Green' for x in range(high)])

#Quits out of the program
def stop():
    root.quit()

#Creating the UI
#The window
window = Frame(root, width=800, height=500, bg="Grey")
window.grid(row=0, column=0, padx=10, pady=5)

#The canvas
canvas = Canvas(root, width=800, height=500, bg="Grey")
canvas.grid(row=1, column=0, padx=10, pady=5)

#Creating a user interface in grid manner
#First row components
Label(window, text="Algorithm", bg="Grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)

#Algorithm to show the name of the sorting algorithm
alg_Menu = ttk.Combobox(window, textvariable=select_Alg, values=["Bubble Sort", "Quick Sort", "Selection Sort", "Heap Sort"])
alg_Menu.grid(row=0, column=1, padx=5, pady=5)
alg_Menu.current(0)

#Creating the start and stop button
Button(window, text="Start", bg="Blue", command=start_Algorithm).grid(row=2, column=0, padx=5, pady=5)
Button(window, text="Stop", bg="Red", command=stop).grid(row=2, column=1, padx=5, pady=5)

#Creating the speed bar using scale
speedbar = Scale(window, from_=0.0, to=0.5, length=100, digits=2,
 resolution=0.01, orient=HORIZONTAL, label="Select Speed")
speedbar.grid(row=0, column=2, padx=5, pady=5)

#Second row components
#size_Entry: scale to select the size of the data bars
size_Entry = Scale(window, from_=3, to=35, resolution=1,
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
Button(window, text="Generate", bg="Green", command=generate_Values).grid(row=0, column=3, padx=5, pady=5)

#Stopping the main loop
root.mainloop()

#endregion