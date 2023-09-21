import numpy as np


class RotationsManager:

    def __init__(self, file_manager, gui, data, redrawer):

        self.file_manager = file_manager
        self.gui = gui
        self.data = data
        self.redrawer = redrawer

    def rotate_left(self, event):

        self.gui.second_ax.clear()

        self.data.second_data = np.rot90(self.data.second_data)

        self.redrawer.redraw()

    def rotate_right(self, event):

        self.gui.second_ax.clear()

        self.data.second_data = np.rot90(self.data.second_data)
        self.data.second_data = np.rot90(self.data.second_data)
        self.data.second_data = np.rot90(self.data.second_data)

        self.redrawer.redraw()
