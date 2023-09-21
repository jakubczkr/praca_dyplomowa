import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Gui:

    def __init__(self, config):

        # create root
        self.root = tk.Tk()
        self.root.title(config.window_title)
        self.root.geometry(config.window_size)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)

        # first columns name ComboBox
        self.first_selected_column = tk.StringVar()
        self.first_columns_cb = ttk.Combobox(self.root, textvariable=self.first_selected_column)
        self.first_columns_cb.pack(fill=tk.X, padx=5, pady=5)
        self.first_columns_cb['state'] = 'readonly'

        # second columns name ComboBox
        self.second_selected_column = tk.StringVar()
        self.second_columns_cb = ttk.Combobox(self.root, textvariable=self.second_selected_column)
        self.second_columns_cb.pack(fill=tk.X, padx=5, pady=5)
        self.second_columns_cb['state'] = 'readonly'

        # first image plot
        self.first_figure, self.first_ax = plt.subplots(1, 1)
        self.first_canvas = FigureCanvasTkAgg(self.first_figure, self.root)
        self.first_canvas.get_tk_widget().pack()

        # second image plot
        self.second_figure, self.second_ax = plt.subplots(1, 1)
        self.second_canvas = FigureCanvasTkAgg(self.second_figure, self.root)
        self.second_canvas.get_tk_widget().pack()

        # buttons
        self.left_rotate_button = tk.Button(self.root, text="Obróć w lewo")
        self.left_rotate_button.pack()

        self.transform_button = tk.Button(self.root, text="Transformacja")
        self.transform_button.pack()

        self.right_rotate_button = tk.Button(self.root, text="Obróć w prawo")
        self.right_rotate_button.pack()

        self.clear_button = tk.Button(self.root, text="Wyczyść")
        self.clear_button.pack()
