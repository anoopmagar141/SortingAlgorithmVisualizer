import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generate_data():
    """Generate random dataset for sorting."""
    global data
    data = [random.randint(1, 100) for _ in range(20)]
    draw_data(data, ['blue' for _ in range(len(data))])

def draw_data(data, color_array):
    """Draws the dataset as a bar chart."""
    ax.clear()
    ax.bar(range(len(data)), data, color=color_array)
    canvas.draw()
    root.update_idletasks()  # Smooth UI update

def bubble_sort():
    """Perform Bubble Sort and visualize it."""
    global data
    n = len(data)
    if n == 0:
        messagebox.showerror("Error", "No data to sort!")
        return

    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['red' if x == j or x == j+1 else 'blue' for x in range(n)])
                time.sleep(0.05)

    draw_data(data, ['green' for _ in range(n)])
