from . import (
    pyplot_plotting,
    tkinter_plotting
)
from ..gui_engines import GuiEngine
from .. import bedbug as bd


def plot_manager(gui_engine: GuiEngine = GuiEngine.default, plot_group: str = None) -> None:
    """
    Plot all variables in plot_group with the selected GUI engine.
    Currently, the default and only engine is 'pyplot'.
    :param gui_engine: the selected engine for plotting the data
    :param plot_group: the name of the group for plotting its variables, or None for plotting all variables.
    The default value is None.
    :return: None
    """
    signals: list[tuple[str, str]] = []
    if plot_group == None:
        for group_name in bd._groups.keys():
            for var_name in bd.get_group(group_name).vars.keys():
                signals.append((group_name, var_name))
    else:
        for var_name in bd.get_group(plot_group).vars.keys():
            signals.append((plot_group, var_name))

    if gui_engine == GuiEngine.PyPlot:
        pyplot_plotting.plot(signals)
    elif gui_engine == GuiEngine.tkinter:
        tkinter_plotting.plot(signals)
    else:
        # TODO
        pass
