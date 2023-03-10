"""
Credit: https://www.geeksforgeeks.org/bubble-sort-visualizer-using-pygame/
"""

import pygame as pyg
import numpy as np

pyg.init()

#Sets the window size
window = pyg.display.set_mode((500, 400))

#Sets the caption
pyg.display.set_caption("Bubble Sort")

#Initial position
x = 40
y = 40

#Width and height of each bar
width = 20
height = np.random.randint(1, 275, 15)

run = True

#Bubble Sort Function
def bubble_Sort(height):

    #Iterates through the heights
    for i in range(len(height) - 1):
        for j in range(len(height) - i - 1):

            #When the height of j is greater than j + 1
            if height[j] > height[j + 1]:
                
                #Swaps the heights
                height[j], height[j + 1] = height[j + 1], height[j]

def quick_Sort(heigths, low, high):

    #Finds the pivot 
    pi = partition(heights, low, high)

    #Sorts on the left side
    quick_Sort(heigths, low, pi - 1)

    #Sorts on the right side
    quick_Sort(heigths, pi + 1, high)
    
def partition(heights, low, high):
    
    #Creates a pivot
    pivot = heights[high]

    #Pointer to greater element
    i = low - 1

    #Iterates through the heights and checks j with the pivot
    for j in range(low, high):
        if heights[j] <= pivot:

            #Sets i to the greater element
            i += 1

            #Swaps the elements
            heights[i], heights[j] = heights[j], heights[i]
    
    #Swaps teh pivot
    heights[i + 1], heights[high] = heights[high], heights[i + 1]

    #Returns the position
    return i + 1

#Function to show the heights of the given list
def show(height):

    #Iterates through height
    for i in range(len(height)):

        #Draws the respected bars with a gap
        pyg.draw.rect(window, (255, 0, 0), (x + 30 * i, y, width, height[i]))

#Keeps the game running
while run:

    #Starts the sorting
    execute = False

    #Adds a delay
    pyg.time.delay(10)

    #Sets up the keys pressed
    keys = pyg.key.get_pressed()

    #Iterates through the events
    for event in pyg.event.get():

        #Quits game, breaking out of the loop
        if event.type == pyg.QUIT:
            run = False
        
    #Runs the sort if space is pressed
    if keys[pyg.K_SPACE]:
        execute = True

    #When execute is set to false
    if execute == False:

        #Fills the window with black
        window.fill((0, 0, 0))

        #Shows the list of heights
        show(height)

        #Updates the window
        pyg.display.update()

    #When execute is set to true
    else:

        #Bubble Sort
        bubble_Sort(height)

        #Fills the window with black
        window.fill((0, 0, 0))

        #Shows the list of heights
        show(height)

        #Adds a delay
        pyg.time.delay(50)

        #Updates the display
        pyg.display.update()

#Exits the visualizer
pyg.quit()