import pandas as pd
import numpy as np


# noinspection PyArgumentList,PyMethodMayBeStatic
class FileManager:

    def read(self, file_path, column_name):

        dfs = pd.read_excel(file_path)

        dfs.sort_values(by=['x', 'y'], inplace=True)
        dfs = dfs.reset_index(drop=True)

        x_size = dfs['y'].value_counts().values[0]
        y_size = dfs['x'].value_counts().values[0]

        data = np.zeros((x_size, y_size))

        index_x = []
        index_y = []

        for i in range(x_size):
            for j in range(y_size):

                data[i, j] = dfs[column_name][i * y_size + j]
                if data[i, j] > 250:
                    data[i, j] = 250

                index_x.append(i)
                index_y.append(j)

        dfs['X_index'] = index_x
        dfs['Y_index'] = index_y

        return np.transpose(data), dfs

    def save(self, file_path, data_frame, column_name, new_data):

        data_frame[column_name] = np.transpose(new_data).flatten()

        data_frame = data_frame.drop(columns=['X_index', 'Y_index'])

        data_frame.to_excel(file_path, index=False)

    def combine_saves(self, first_file_path, first_data_frame, first_column_name, first_new_data,
                      second_file_path, second_data_frame, second_column_name, second_new_data):

        self.save(first_file_path, first_data_frame, first_column_name, first_new_data)
        self.save(second_file_path, second_data_frame, second_column_name, second_new_data)

