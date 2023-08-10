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
