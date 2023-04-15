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
    for groupname in bd._groups.keys():
        for varname in bd._groups[groupname].vars.keys():
            signals.append((groupname, varname))
    num_of_signals = len(signals)
    ax1 = None
    for signal in range(num_of_signals):
        if signal == 0:
            ax1 = plt.subplot(num_of_signals, 1, signal + 1)
        else:
            ax1 = plt.subplot(num_of_signals, 1, signal + 1, sharex=ax1)
        plt.plot()