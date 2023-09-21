import numpy as np


class PointsManager:

    def __init__(self, data, gui, coordinates_calculator, file_manager, transformation_manager, redrawer, config):

        self.data = data
        self.gui = gui
        self.coordinates_calculator = coordinates_calculator
        self.file_manager = file_manager
        self.transformation_manager = transformation_manager
        self.redrawer = redrawer
        self.config = config

        self.drawn_points = []

    def clear(self, event):

        self.data.first_points = []
        self.data.second_points = []

        for point in self.drawn_points:
            point[0].remove()

        self.drawn_points = []

        self.redrawer.redraw()

    def get_rectangle(self, points):

        if len(points) < 2:
            return [[], []]

        arr = np.array(points)
        return [
            [int(round(np.min(arr[:, 0]))), int(round(np.max(arr[:, 0])))],
            [int(round(np.min(arr[:, 1]))), int(round(np.max(arr[:, 1])))]
        ]

    def add_to_plot(self, x, y, canvas, ax):
        point = ax.plot(x, y, color=self.config.marker_color, marker=self.config.marker_style, linestyle="",
                        markersize=self.config.marker_size)
        self.drawn_points.append(point)
        canvas.draw()

    def first_save_point_coordinates(self, event):
        self.add_to_plot(event.xdata, event.ydata, self.gui.first_canvas, self.gui.first_ax)
        self.data.first_points.append([event.xdata, event.ydata])

    def second_save_point_coordinates(self, event):
        self.add_to_plot(event.xdata, event.ydata, self.gui.second_canvas, self.gui.second_ax)
        self.data.second_points.append([event.xdata, event.ydata])

    def get_points(self, event):

        first_rectangle = self.get_rectangle(self.data.first_points)
        second_rectangle = self.get_rectangle(self.data.second_points)

        self.data.first_x_lims, self.data.second_x_lims = self.coordinates_calculator.calculate(
            [first_rectangle[0][0], first_rectangle[0][1], self.data.first_data.shape[1]],
            [second_rectangle[0][0], second_rectangle[0][1], self.data.second_data.shape[1]])

        self.data.first_y_lims, self.data.second_y_lims = self.coordinates_calculator.calculate(
            [first_rectangle[1][0], first_rectangle[1][1], self.data.first_data.shape[0]],
            [second_rectangle[1][0], second_rectangle[1][1], self.data.second_data.shape[0]])

        self.transformation_manager.transform()
