import matplotlib.pyplot as plt
from .const import PlotConst
from .. import (
    bedbug as bd,
    const
)


def get_signal_name(groupname, varname):
    if groupname == const.DEFAULT_GROUP_NAME:
        return varname
    return f"{groupname}/{varname}"


def get_values_from_pair_list(time_value_pair_list: list, num_of_time_ticks: int) -> list:
    # Initialize values
    values = [PlotConst.EMPTY_VALUE] * num_of_time_ticks
    # Fill registered values
    for time_index, value in time_value_pair_list:
        values[time_index] = value
    # Fill empty values with last value, if any
    value_exists_before = False
    first_index_with_value = -1
    for time_index in range(num_of_time_ticks):
        if values[time_index] == PlotConst.EMPTY_VALUE:
            if value_exists_before:
                values[time_index] = values[time_index - 1]
        else:
            if not value_exists_before:
                value_exists_before = True
                first_index_with_value = time_index
    # Fill initial empty values with first value
    value_exists_before = False
    for time_index in range(first_index_with_value):
        values[time_index] = values[first_index_with_value]
    return values


def plot():
    signals: list[tuple[str, str]] = []
    for group_name in bd._groups.keys():
        for var_name in bd.get_group(group_name).vars.keys():
            signals.append((group_name, var_name))
    num_of_signals: int = len(signals)
    
    ax1: plt.Axes = None
    num_of_time_ticks = bd.time.current_time
    t = range(num_of_time_ticks)
    for signal in range(num_of_signals):
        group_name = signals[signal][0]
        var_name = signals[signal][1]
        signal_name = get_signal_name(group_name, var_name)
        group = bd.get_group(group_name)
        time_value_pair_list = group.vars[var_name]

        values = get_values_from_pair_list(time_value_pair_list, num_of_time_ticks)
        
        if signal == 0:
            ax1 = plt.subplot(num_of_signals, 1, signal + 1)
        else:
            plt.subplot(num_of_signals, 1, signal + 1, sharex=ax1)
        
        plt.plot(t, values)
        plt.ylabel(signal_name, rotation = 0)
    
    plt.show()
