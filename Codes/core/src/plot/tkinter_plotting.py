from .tkinter.classes import TK_GUI, TkPlotterWindow

def plot(signals: list[tuple[str, str]]) -> None:
    """
    Plot all variables in the input list with tkinter GUI engine.
    :param signals: a list of (group name, variable name) pairs
    :type signals: list[tuple[str, str]]
    """
    TK_GUI = TkPlotterWindow("tk GUI")
    TK_GUI.tk_element.mainloop()
    print('Meow')
