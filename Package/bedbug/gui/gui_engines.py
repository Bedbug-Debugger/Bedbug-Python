from enum import Enum


class GuiEngine(Enum):
    PyPlot = "pyplot"
    tkinter = "tkinter"
    default = tkinter
