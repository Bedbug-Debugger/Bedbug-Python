from ...src import bedbug as bd


def test_with_default_group_and_one_variable():
    index = 0
    while index <= 10:
        index += 1
        bd.add_data("index", index)
    print(bd.get_group(bd.const.DEFAULT_GROUP_NAME).signals)
    bd.plot(gui_engine=bd.GuiEngine.PyPlot)


def test_with_default_group_and_two_vars_and_pause():
    a = 0
    b = 0
    bd.add_data_multi({
        "a": a
    })
    print(bd.get_group(bd.const.DEFAULT_GROUP_NAME).signals)
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
    print(bd.get_group(bd.const.DEFAULT_GROUP_NAME).signals)
    bd.time.pause()
    a = 17
    bd.add_data("a", a)
    b = 19
    bd.add_data("b", b)
    bd.time.resume()
    print(bd.get_group(bd.const.DEFAULT_GROUP_NAME).signals)
    a = 23
    bd.add_data("a", a)
    print(bd.get_group(bd.const.DEFAULT_GROUP_NAME).signals)
    bd.plot(gui_engine=bd.GuiEngine.PyPlot)


def test_with_multiple_groups_and_multiple_vars():
    a, b, c = 1, 2, 3
    G1 = bd.create_group("G1")
    G1.add_data("a", a)
    print("Did G1\n")
    G2 = bd.create_group("G2")
    G2.add_data("b", b)
    print("Did G2\n")
    G3 = bd.create_group("G3")
    G3.add_data("c", c)
    print("Did G3\n")
    bd.plot(gui_engine=bd.GuiEngine.PyPlot)
    G2.plot(gui_engine=bd.GuiEngine.PyPlot)

def run():
    test_with_default_group_and_one_variable()
    # test_with_default_group_and_two_vars_and_pause()
    # test_with_multiple_groups_and_multiple_vars()
