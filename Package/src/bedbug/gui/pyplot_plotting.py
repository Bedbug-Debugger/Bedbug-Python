from typing import Union

import matplotlib.pyplot as plt
import numpy as np

from . import plot_utility
from ..models.wrappers import (
    GroupSignalPair,
    SignalRecord,
    TimeTick
)
from .. import bedbug as bd


def get_axes(axs: Union[plt.Axes, np.ndarray], num_of_signals: int, signal_num: int) -> plt.Axes:
    if num_of_signals == 1:
        return axs
    return axs[signal_num]

def plot_single_signal(ax: plt.Axes, time_ticks: list[TimeTick], signal_label: str, signal_record: SignalRecord):
    time_list: list[int] = []
    value_list: list[float] = []
    # Add relevant (time_tick, value) points to time_list and value_list for plotting
    for time_tick in time_ticks:
        if time_tick in signal_record:
            value = signal_record[time_tick]
            time_list.append(time_tick.time)
            value_list.append(float(value.value))
    # Add sentinel element to time_list and value_list, needed for the tail of the plot
    time_list.append(time_ticks[-1].time + 1)    # time_ticks is referred to, so that all plots end in the same time tick
    value_list.append(value_list[-1])
    ax.step(time_list, value_list, 'b', where='post')
    ax.plot(time_list[:-1], value_list[:-1], 'bo')
    ax.set_ylabel(signal_label + 4*' ', rotation='horizontal')

def plot(signals: list[GroupSignalPair]) -> None:
    """
    Plot all variables in the input list with pyplot's GUI engine.
    :param signals: List of signal labels in GroupSignalPair format
    :type signals: list[GroupSignalPair]
    """
    time_ticks: list[TimeTick] = plot_utility.get_time_ticks(signals)
    num_of_signals = len(signals)
    fig, axs = plt.subplots(num_of_signals, 1, sharex=True)
    # Draw signals in different subplots
    for signal_num in range(num_of_signals):
        signal = signals[signal_num]
        group_name = signal.group_name
        signal_label = signal.signal_label
        signal_full_label = plot_utility.get_signal_full_label(group_name, signal_label)
        group = bd.get_group(group_name.name)
        signal_record = group.signals[signal_label]
        this_ax = get_axes(axs, num_of_signals, signal_num)
        plot_single_signal(this_ax, time_ticks, signal_full_label, signal_record)
    # Set time axis values
    last_ax = get_axes(axs, num_of_signals, num_of_signals-1)
    last_ax.set_xticks([tick.time for tick in time_ticks])
    plt.show()



# def plot(signals: list[tuple[str, str]]) -> None:
#     """
#     Plot all variables in the input list with pyplot's GUI engine.
#     :param signals: a list of (group name, variable name) pairs
#     :return: None
#     """
#     num_of_signals: int = len(signals)
#     ax1: plt.Axes = None
#     num_of_time_ticks = bd.time.current_time
#     t = range(num_of_time_ticks)
#     for signal in range(num_of_signals):
#         group_name = signals[signal][0]
#         var_name = signals[signal][1]
#         signal_name = plot_utility.get_signal_name(group_name, var_name)
#         group = bd.get_group(group_name)
#         time_value_dict = group.vars[var_name]

#         values = plot_utility.get_values_from_dict(time_value_dict, num_of_time_ticks)

#         if signal == 0:
#             ax1 = plt.subplot(num_of_signals, 1, signal + 1)
#         else:
#             plt.subplot(num_of_signals, 1, signal + 1, sharex=ax1)

#         plt.plot(t, values, 'b')
#         for time_index, val in time_value_dict.items():
#             plt.plot(time_index, val, 'ro')
#         plt.ylabel(signal_name, rotation=0)

#     plt.show()
