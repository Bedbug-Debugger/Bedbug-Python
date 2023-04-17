import matplotlib.pyplot as plt
from . import plot_utility
from .. import bedbug as bd


def plot(signals: list[tuple[str, str]]) -> None:
    """
    Plot all variables in the input list with pyplot's GUI engine.
    :param signals: a list of (group name, variable name) pairs
    :return: None
    """
    num_of_signals: int = len(signals)
    ax1: plt.Axes = None
    num_of_time_ticks = bd.time.current_time
    t = range(num_of_time_ticks)
    for signal in range(num_of_signals):
        group_name = signals[signal][0]
        var_name = signals[signal][1]
        signal_name = plot_utility.get_signal_name(group_name, var_name)
        group = bd.get_group(group_name)
        time_value_dict = group.vars[var_name]

        values = plot_utility.get_values_from_dict(time_value_dict, num_of_time_ticks)

        if signal == 0:
            ax1 = plt.subplot(num_of_signals, 1, signal + 1)
        else:
            plt.subplot(num_of_signals, 1, signal + 1, sharex=ax1)

        plt.plot(t, values, 'b')
        for time_index, val in time_value_dict.items():
            plt.plot(time_index, val, 'ro')
        plt.ylabel(signal_name, rotation=0)

    plt.show()
