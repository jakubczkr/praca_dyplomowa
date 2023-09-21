import tkinter as tk
from functools import partial

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class TransformedGui:

    def __init__(self, file_manager, data, gui, config):

        self.file_manager = file_manager
        self.data = data
        self.gui = gui
        self.config = config

        root = tk.Tk()
        root.title("Rozkłady po transformacji")

        figure, ax = plt.subplots(1, 2)

        ax[0].imshow(self.data.first_data_reduced, cmap=self.config.colormap)
        ax[1].imshow(self.data.second_data_resized, cmap=self.config.colormap)

        canvas = FigureCanvasTkAgg(figure, root)
        canvas.get_tk_widget().pack()

        save_button = tk.Button(root, text="Zapisz do pliku",
                                command=partial(self.file_manager.combine_saves,
                                                self.data.first_file_name, self.data.first_data_frame,
                                                self.gui.second_columns_cb.get(), self.data.first_data_copy,
                                                self.data.second_file_name, self.data.second_data_frame,
                                                self.gui.first_columns_cb.get(), self.data.second_data_copy))

        save_button.pack()
