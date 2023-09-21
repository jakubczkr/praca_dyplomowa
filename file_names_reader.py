from tkinter import filedialog


# noinspection PyMethodMayBeStatic
class FileNamesReader:

    def get_file_names(self):

        first_file_name = filedialog.askopenfilename()
        second_file_name = filedialog.askopenfilename()

        return first_file_name, second_file_name
