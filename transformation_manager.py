import numpy as np
from skimage.transform import resize

from tranformed_gui import TransformedGui


# noinspection DuplicatedCode
class TransformationManager:

    def __init__(self, file_manager, data, gui, config):

        self.file_manager = file_manager
        self.data = data
        self.gui = gui
        self.config = config

    def transform(self):

        self.data.first_data_reduced = self.data.first_data[self.data.first_y_lims[0]: self.data.first_y_lims[1],
                                       self.data.first_x_lims[0]: self.data.first_x_lims[1]]
        self.data.second_data_reduced = self.data.second_data[self.data.second_y_lims[0]: self.data.second_y_lims[1],
                              self.data.second_x_lims[0]: self.data.second_x_lims[1]]

        self.data.second_data_resized = resize(self.data.second_data_reduced,
                                               (len(self.data.first_data_reduced), len(self.data.first_data_reduced[0])))

        self.data.first_data_copy = np.copy(self.data.first_data)
        self.data.first_data_copy.fill(0)
        self.data.first_data_copy[self.data.first_y_lims[0]: self.data.first_y_lims[1],
            self.data.first_x_lims[0]: self.data.first_x_lims[1]] = self.data.second_data_resized

        self.data.second_data_copy = np.copy(self.data.second_data)
        self.data.second_data_copy.fill(0)
        self.data.second_data_copy[self.data.second_y_lims[0]: self.data.second_y_lims[1],
            self.data.second_x_lims[0]: self.data.second_x_lims[1]] = self.data.second_data_reduced

        TransformedGui(self.file_manager, self.data, self.gui, self.config)
