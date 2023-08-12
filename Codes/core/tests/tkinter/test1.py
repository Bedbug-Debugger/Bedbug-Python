from ...src import (
    bedbug as bd
)
from ...src.plot import (
    tkinter_plotting as tkp
)

def empty_window():
    tkp.open_window()

def first_window():
    a = 3
    b = 2
    c = 1
    bd.add_data_multi({
        'a': a,
        'b': b,
        'c': c
    })
    bd.plot()
    print('Meow')

def multi_tick():
    a = 1
    bd.add_data('a', a)
    b = 2
    bd.add_data('b', b)
    c = 3
    bd.add_data('c', c)
    a = 4
    bd.add_data('a', a)
    bd.plot()

def run():
    # empty_window()
    # first_window()
    multi_tick()
