from .tkinter.classes import TK_GUI, TkPlotterWindow

def open_window():
    TK_GUI = TkPlotterWindow("tk GUI")
    TK_GUI.tk_element.mainloop()
    print('Meow')
