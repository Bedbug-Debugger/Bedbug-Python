from typing import Union

import matplotlib.pyplot as plt
import numpy as np

from .const import PlotConst
from .. import const
from .. import bedbug as bd


def get_signal_name(groupname: str, varname: str) -> str:
    """
    Return a "groupname/varname" string based on groupname and varname, or "varname" if the group is the default group.
    :param groupname: the name of the group
    :param varname: the name of the variable in the group
    :return: "groupname/varname"
    """
    if groupname == const.DEFAULT_GROUP_NAME:
        return varname
    return f"{groupname}/{varname}"

def get_time_ticks(signals: list[tuple[str, str]]) -> list:
    """
    Find all time ticks when at least one data was added.
    :param signals: List of all signals to search in
    :type signals: list[tuple[str, str]]
    :return: List of all extracted time ticks, in ascending order
    :rtype: list
    """
    time_ticks = set()  # set is used to prevent adding duplicate time ticks
    for signal in signals:
        group_name = signal[0]
        var_name = signal[1]
        group = bd.get_group(group_name)
        time_value_dict = group.vars[var_name]
        for time_tick in time_value_dict:
            time_ticks.add(time_tick)
    time_ticks = list(time_ticks)
    time_ticks.sort()
    return time_ticks

def get_axes(axs: Union[plt.Axes, np.ndarray], num_of_signals: int, signal_num: int) -> plt.Axes:
    if num_of_signals == 1:
        return axs
    return axs[signal_num]

def plot_single_signal(ax: plt.Axes, time_ticks: list, signal_name: str, time_value_dict: dict):
    time_list = []
    value_list = []
    # Add relevant (time_tick, value) points to time_list and value_list for plotting
    for time_tick in time_ticks:
        if time_tick in time_value_dict:
            value = time_value_dict[time_tick]
            time_list.append(time_tick)
            value_list.append(value)
    # Add sentinel element to time_list and value_list, needed for the tail of the plot
    time_list.append(time_ticks[-1] + 1)    # time_ticks is referred to, so that all plots end in the same time tick
    value_list.append(value_list[-1])
    ax.step(time_list, value_list, 'b', where='post')
    ax.plot(time_list[:-1], value_list[:-1], 'bo')
    ax.set_ylabel(signal_name + 4*' ', rotation='horizontal')



# def get_values_from_dict(time_value_dict: dict, num_of_time_ticks: int) -> list:
#     """
#     Return the list of values of a variable in all sampling time ticks, based on the variable's value dictionary.
#     :param time_value_dict: the value dictionary of the variable, in the form of {time_tick: value}
#     :param num_of_time_ticks: the number of time ticks until calling this function
#     :return: list of values of the variable
#     """
#     # Initialize values
#     values = [PlotConst.EMPTY_VALUE] * num_of_time_ticks
#     # Fill registered values
#     for time_index, value in time_value_dict.items():
#         values[time_index] = value
#     # Fill empty values with last value, if any
#     value_exists_before = False
#     first_index_with_value = -1
#     for time_index in range(num_of_time_ticks):
#         if values[time_index] == PlotConst.EMPTY_VALUE:
#             if value_exists_before:
#                 values[time_index] = values[time_index - 1]
#         else:
#             if not value_exists_before:
#                 value_exists_before = True
#                 first_index_with_value = time_index
#     # Fill initial empty values with first value
#     value_exists_before = False
#     for time_index in range(first_index_with_value):
#         values[time_index] = values[first_index_with_value]
#     return values
