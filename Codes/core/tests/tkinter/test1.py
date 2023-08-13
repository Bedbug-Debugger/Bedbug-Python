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

def multi_data():
    a = 1
    bd.add_data('a', a)
    b = 'abcdefghijk'
    bd.add_data('b', b)
    c = 3
    d = 's'
    bd.add_data_multi({
        'c': c,
        'd': d
    })
    a = 4
    bd.add_data('a', a)
    bd.plot()

def long_history():
    for i in range(100):
        a = i + 1
        b = i * 2
        c = i // 2
        bd.add_data_multi({
            'i': i,
            'a': a,
            'b': b,
            'c': c
        })
    bd.plot()

def run():
    # empty_window()
    # first_window()
    # multi_tick()
    multi_data()
    # long_history()
