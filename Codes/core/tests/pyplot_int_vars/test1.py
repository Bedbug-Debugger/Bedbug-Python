from ...src import (
    bedbug as bd,
    const
)


def test_with_default_group_and_one_variable():
    index = 0
    while index <= 10:
        index += 1
        bd.add_data(index, "index")
    print(bd.get_group(const.DEFAULT_GROUP_NAME).vars)


def run():
    test_with_default_group_and_one_variable()
    bd.plot()
