class ColumnsManager:

    def __init__(self, file_manager, gui, data, config):

        self.config = config
        self.file_manager = file_manager
        self.gui = gui
        self.data = data

    def first_column_changed(self, event):

        self.data.first_data, self.data.first_data_frame = self.file_manager.read(
            self.data.first_file_name, self.gui.first_columns_cb.get())
        self.gui.first_ax.imshow(self.data.first_data, cmap=self.config.colormap)
        self.gui.first_canvas.draw()

    def second_column_changed(self, event):

        self.data.second_data, self.data.second_data_frame = self.file_manager.read(self.data.second_file_name, self.gui.second_columns_cb.get())
        self.gui.second_ax.imshow(self.data.second_data, cmap=self.config.colormap)
        self.gui.second_canvas.draw()
