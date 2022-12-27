"""
Credit: https://www.geeksforgeeks.org/visualizing-bubble-sort-using-python/?ref=rp
-- Used for the visualizer aspect
"""

import random
import numpy as np
from matplotlib import pyplot as plt, animation

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

#Visualizers
def visualize():
    n = 30
    lengths = np.random.randint(1, 275, n)
    random.shuffle(lengths)

    #Creates a generator object that contains the lengths
    generator = bubble_Sort(lengths)

    #Creates the figures and subplots
    figure, axis = plt.subplots()
    axis.set_title("Bubble Sort O(n\N{SUPERSCRIPT TWO})")
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
        frames=generator,
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