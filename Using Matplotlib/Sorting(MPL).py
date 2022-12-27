"""
Credit: https://www.geeksforgeeks.org/visualizing-bubble-sort-using-python/?ref=rp
-- Used for the visualizer aspect
"""

import random
import numpy as np
from matplotlib import pyplot as plt, animation

#Bubble Sort Algorithm
def bubble_Sort(lengths):
     
    #Iterates through the lengths
    for i in range(len(lengths) - 1):
        for j in range(len(lengths) - i - 1):
            
            #Swaps j and j + 1
            if lengths[j] > lengths[j + 1]:
                temp = lengths[j]
                lengths[j] = lengths[j + 1]
                lengths[j + 1] = temp
            
            yield lengths

#Quick Sort Algorithm
def quick_Sort(lengths, low, high):
    if low < high:

        #Finds the element
        pi = partition(lengths, low, high)

        #For the left side
        quick_Sort(lengths, low, pi - 1)

        #For the right side
        quick_Sort(lengths, pi + 1, high)

def partition(lengths, low, high):
    #Sets the pivot
    pivot = lengths[high]

    #Pointer for the greater element
    i = low - 1

    #Iterates through the elements and compares the pivot
    for j in range(low, high):
        if lengths[j] <= pivot:

            #Swaps the elements
            i += 1
            lengths[i], lengths[j] = lengths[j],lengths[i]

        #Swaps the pivot with high
        lengths[i + 1], lengths[high] = lengths[high], lengths[i + 1]

    #Returns the position
    return i + 1

#Visualizers
def visualize():
    n = 30
    lengths = np.random.randint(1, 275, n)
    low = 0
    high = len(lengths)
    random.shuffle(lengths)

    #Creates a generator object that contains the lengths
    generator_Bubble = bubble_Sort(lengths)
    generator_Quick = quick_Sort(lengths, low, high - 1)

    #Creates the figures and subplots
    figure, axis = plt.subplots()
    axis.set_title("Sort O(n\N{SUPERSCRIPT TWO})")
    bar_Sub = axis.bar(range(len(lengths)), lengths, align="edge")

    #Sets the max for the x-axis
    axis.set_xlim(0, n)
    text = axis.text(0.02, 0.95, "", transform=axis.transAxes)
    iteration = [0]

    #Helper function for updating
    def update(lengths, rects, iteration):
        for rect, val in zip(rects, lengths):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")

    #Creates an animation object
    anim = animation.FuncAnimation(
        figure, 
        func=update,
        fargs=(bar_Sub, iteration),
        frames=generator_Bubble,
        repeat=True,
        blit=False,
        interval=15,
        save_count=90000,
    )

    #Shows the animation on the screen
    plt.show()
    plt.close()

if __name__ == "__main__":
    visualize()