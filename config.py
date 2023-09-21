import configparser


class Config:

    def __init__(self):
        self.marker_size = None
        self.marker_color = None
        self.marker_style = None
        self.colormap = None
        self.window_size = None
        self.window_title = None

    def read_config(self):

        config_file_name = 'config.txt'
        config = configparser.ConfigParser()
        config.read(config_file_name)

        self.window_title = config['CONFIG']['window_title']
        self.window_size = config['CONFIG']['window_size']
        self.colormap = config['CONFIG']['colormap']
        self.marker_style = config['CONFIG']['marker_style']
        self.marker_color = config['CONFIG']['marker_color']
        self.marker_size = config['CONFIG']['marker_size']

