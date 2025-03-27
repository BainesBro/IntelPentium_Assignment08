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
