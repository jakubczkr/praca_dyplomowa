import numpy as np


class Data:

    def __init__(self):

        self.first_data = np.zeros((20, 20))
        self.second_data = np.zeros((20, 20))

        self.first_data_frame = None
        self.second_data_frame = None

        self.first_points = []
        self.second_points = []

        self.first_file_name = ""
        self.second_file_name = ""
