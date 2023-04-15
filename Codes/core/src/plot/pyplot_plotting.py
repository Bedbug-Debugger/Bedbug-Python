import matplotlib.pyplot as plt
from .. import (
    bedbug as bd,
    const
)


def get_signal_name(groupname, varname):
    if groupname == const.DEFAULT_GROUP_NAME:
        return varname
    return f"{groupname}/{varname}"


def plot():
    signals: list[tuple[str, str]] = []
    for group_name in bd._groups.keys():
        for var_name in bd.get_group(group_name).vars.keys():
            signals.append((group_name, var_name))
    num_of_signals: int = len(signals)
    
    ax1: plt.Axes = None
    t = range(bd.time.current_time)
    for signal in range(num_of_signals):
        group_name = signals[signal][0]
        var_name = signals[signal][1]
        signal_name = get_signal_name(group_name, var_name)
        group = bd.get_group(group_name)
        values = group.vars[var_name]

        if signal == 0:
            ax1 = plt.subplot(num_of_signals, 1, signal + 1)
        else:
            plt.subplot(num_of_signals, 1, signal + 1, sharex=ax1)
        
        plt.plot(t, values)
        plt.ylabel(signal_name, rotation = 0)
    
    plt.show()
