import bedbug as bd

def func1():
	a = 1
	bd.add_data('a', a)
	b = 2
	c = 3
	bd.add_data_multi({
		'b': b,
		'c': c
	})
	a = 4
	bd.add_data('a', a)
	bd.plot()

def test_run():
	func1()
