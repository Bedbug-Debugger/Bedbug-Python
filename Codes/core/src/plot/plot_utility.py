from ..models.group import (
    SignalLabel,
    GroupName,
    GroupSignalPair
)
from .. import const
from ..models.time_manager import TimeTick
from .. import bedbug as bd


def get_signal_full_label(group_name: GroupName, signal_label: SignalLabel) -> str:
    """
    Return a "group_name/signal_label" string based on groupname and varname, or "varname" if the group is the default group.
    :param groupname: Name of the group.
    :type group_name: GroupName
    :param signal_label: Label of the signal in the group.
    :type signal_label: SignalLabel
    :return: "group_name/signal_label"
    :rtype: str
    """
    if group_name.name == const.DEFAULT_GROUP_NAME:
        return signal_label.label
    return f"{group_name.name}/{signal_label.label}"

def get_time_ticks(signals: list[GroupSignalPair]) -> list[TimeTick]:
    """
    Find all time ticks when at least one data was added.
    :param signals: List of all signals to search in.
    :type signals: list[GroupSignalPair]
    :return: List of all extracted time ticks, in ascending order.
    :rtype: list[TimeTick]
    """
    time_ticks = set()  # set is used to prevent adding duplicate time ticks
    for signal in signals:
        group_name = signal.group_name
        signal_name = signal.signal_label
        group = bd.get_group(group_name)
        time_value_dict = group.signals[signal_name]
        for time_tick in time_value_dict:
            time_ticks.add(time_tick)
    time_ticks = list(time_ticks)
    time_ticks.sort()
    return time_ticks
