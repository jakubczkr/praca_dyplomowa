from columns_manager import ColumnsManager
from config import Config
from coordinate_calculator import CoordinatesCalculator
from data import Data
from file_manager import FileManager
from file_names_reader import FileNamesReader
from column_names_reader import ColumnNamesReader
from gui import Gui
from points_manager import PointsManager
from redrawer import Redrawer
from rotations_manager import RotationsManager
from transformation_manager import TransformationManager


class App:

    def __init__(self):

        self.config = Config()
        self.config.read_config()
        self.data = Data()

        self.gui = Gui(self.config)

        self.file_names_reader = FileNamesReader()
        self.column_names_reader = ColumnNamesReader()
        self.file_manager = FileManager()
        self.columns_manager = ColumnsManager(self.file_manager, self.gui, self.data, self.config)

        self.coordinates_calculator = CoordinatesCalculator()
        self.redrawer = Redrawer(self.gui, self.data, self.config)
        self.rotations_manager = RotationsManager(self.file_manager, self.gui, self.data, self.redrawer)
        self.transformation_manager = TransformationManager(self.file_manager, self.data, self.gui, self.config)
        self.points_manager = PointsManager(self.data, self.gui, self.coordinates_calculator, self.file_manager,
                                            self.transformation_manager, self.redrawer, self.config)

    def run(self):

        self.data.first_file_name, self.data.second_file_name = self.file_names_reader.get_file_names()

        self.gui.first_columns_cb['values'] = self.column_names_reader.get_column_names(self.data.first_file_name)
        self.gui.second_columns_cb['values'] = self.column_names_reader.get_column_names(self.data.second_file_name)

        self.gui.first_columns_cb.bind('<<ComboboxSelected>>', self.columns_manager.first_column_changed)
        self.gui.second_columns_cb.bind('<<ComboboxSelected>>', self.columns_manager.second_column_changed)

        self.gui.first_ax.imshow(self.data.first_data, cmap=self.config.colormap)
        self.gui.second_ax.imshow(self.data.second_data, cmap=self.config.colormap)

        self.gui.right_rotate_button.bind('<Button-1>', self.rotations_manager.rotate_right)
        self.gui.transform_button.bind('<Button-1>', self.points_manager.get_points)
        self.gui.left_rotate_button.bind('<Button-1>', self.rotations_manager.rotate_left)
        self.gui.clear_button.bind('<Button-1>', self.points_manager.clear)

        self.gui.first_canvas.mpl_connect('button_press_event', self.points_manager.first_save_point_coordinates)
        self.gui.second_canvas.mpl_connect('button_press_event', self.points_manager.second_save_point_coordinates)

        self.gui.root.mainloop()
