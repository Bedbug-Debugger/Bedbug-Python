from .tkinter.classes import TK_GUI, TkWindow

def open_window():
    TK_GUI = TkWindow("tk GUI")
    TK_GUI.tk_element.mainloop()
    print('Meow')
