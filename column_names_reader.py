import pandas as pd


# noinspection PyMethodMayBeStatic,PyArgumentList
class ColumnNamesReader:

    def get_column_names(self, file_path):

        skip_cols = ['x', 'y']
        return pd.read_excel(file_path, usecols=lambda x: x not in skip_cols).columns.tolist()
