class Redrawer:

    def __init__(self, gui, data, config):

        self.gui = gui
        self.data = data
        self.config = config

    def redraw(self):

        self.gui.first_ax.imshow(self.data.first_data, cmap=self.config.colormap)
        self.gui.first_canvas.draw()

        self.gui.second_ax.imshow(self.data.second_data, cmap=self.config.colormap)
        self.gui.second_canvas.draw()
