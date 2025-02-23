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
