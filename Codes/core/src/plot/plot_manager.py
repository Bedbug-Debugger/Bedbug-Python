from . import pyplot_plotting
from ..gui_engines import GuiEngine
from .. import bedbug as bd

def plot_manager(gui_engine: GuiEngine = GuiEngine.PyPlot, plot_group: str = None) -> None:
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
    else:
        # TODO
        pass
