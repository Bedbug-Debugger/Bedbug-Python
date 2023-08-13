# import bedbug as bd
import bedbug as bd

a = 1
b = 2
bd.add_data_multi({
    'a': a,
    'b': b
})
c = 4
bd.add_data('c', c)
bd.plot()
