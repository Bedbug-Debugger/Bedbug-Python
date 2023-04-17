from ...src import (
    bedbug as bd,
    const
)


def test_with_default_group_and_one_variable():
    index = 0
    while index <= 10:
        index += 1
        bd.add_data("index", index)
    print(bd.get_group(const.DEFAULT_GROUP_NAME).vars)
    bd.plot()


def test_with_default_group_and_two_vars_and_pause():
    a = 0
    b = 0
    bd.add_data_multi({
        "a": a
    })
    print(bd.get_group(const.DEFAULT_GROUP_NAME).vars)
    while a < 10:
        bd.add_data_multi({
            "a": a,
            "b": b
        })
        a += 2
        b += 3
    while a < 20:
        bd.add_data("a", a)
        a += 3
    print(bd.get_group(const.DEFAULT_GROUP_NAME).vars)
    bd.time.pause()
    a = 17
    bd.add_data("a", a)
    b = 19
    bd.add_data("b", b)
    bd.time.resume()
    print(bd.get_group(const.DEFAULT_GROUP_NAME).vars)
    a = 23
    bd.add_data("a", a)
    print(bd.get_group(const.DEFAULT_GROUP_NAME).vars)
    bd.plot()


def run():
    # test_with_default_group_and_one_variable()
    test_with_default_group_and_two_vars_and_pause()
