from .tkinter.classes import TK_GUI, TkPlotterWindow

from . import plot_utility

def plot(signals: list[tuple[str, str]]) -> None:
    """
    Plot all variables in the input list with tkinter GUI engine.
    :param signals: a list of (group name, variable name) pairs
    :type signals: list[tuple[str, str]]
    """
    time_ticks = plot_utility.get_time_ticks(signals)
    TK_GUI = TkPlotterWindow("tk GUI", signals=signals)
    TK_GUI.tk_element.mainloop()
    print('Meow')
