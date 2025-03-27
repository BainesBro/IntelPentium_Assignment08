# File Name : Image.py
# Student Name: Collin Baines / Cole Crooks
# email:  bainesct@mail.uc.edu / crookscl@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   03/27/2025
# Course #/Section:   IS4010-002
# Semester/Year:   Spring/2025
# Brief Description of the assignment:  This assignment has us display an image that is related to our team name, and create some sort of visulization

# Brief Description of what this module does. This module creates a graph
# Citations: ChatGPT

# Anything else that's relevant:


import tkinter as tk

# Function to plot a line
def plot_line(canvas, width, height):
    for x in range(0, width):
        y = int(height / 2 + (height / 4) * (x / width - 0.5)**2)  # Quadratic curve: y = (x - 0.5)^2
        canvas.create_oval(x, y, x+1, y+1, fill="blue")

# Set up the window
root = tk.Tk()
root.title("Basic Graph with tkinter")

# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw the graph
plot_line(canvas, 400, 400)

# Run the Tkinter main loop
root.mainloop()
