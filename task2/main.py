import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from laba_logging import *
InitLogFile()
InitFile(__file__)


import tkinter as tk
from graphic import MultiPlotApp


def main():
    root = tk.Tk()
    app = MultiPlotApp(root, "window", "D:\\projects\\VisualStudioCode\\Laba_2_1_5_Graphics\\task1\\task2_data.txt")
    app.categories_name = "дни"
    app.values_name = "коммиты"
    root.mainloop()

if __name__ == "__main__":
    main()