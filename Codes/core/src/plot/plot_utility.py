from .const import PlotConst
from .. import const


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


def get_values_from_dict(time_value_dict: dict, num_of_time_ticks: int) -> list:
    # Initialize values
    values = [PlotConst.EMPTY_VALUE] * num_of_time_ticks
    # Fill registered values
    for time_index, value in time_value_dict.items():
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


