import tkinter as tk
from config import Config


class App:

    def run(self, config: Config):

        root = tk.Tk()
        root.title(config.window_name)
        root.geometry(config.window_size)

        root.mainloop()
