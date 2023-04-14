from ...src import bedbug as bd


def test_with_default_group_and_one_variable():
    index = 0
    while index <= 10:
        index += 1
        bd.add_data(index, "index")


def run():
    test_with_default_group_and_one_variable()
    bd.plot()
