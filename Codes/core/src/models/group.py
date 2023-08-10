from typing import Any

from .time_manager import (
    TimeTick,
    time_ticks_dict,
    time,
    add_new_time_tick
)
from .signal import (
    SignalLabel,
    SignalValue,
    SignalRecord
)
from ..gui_engines import GuiEngine
from ..plot import plot_manager


class GroupName:
	"""
	A wrapper class for group names.
	"""
	def __init__(self, name: str) -> None:
		"""
		Initialize with a label.
		:param label: Signal label
		:type label: str
		"""
		self.name: str = name

class GroupSignalPair:
    """
    A wrapper class for (group name, signal label).
    """
    def __init__(self, group_name: GroupName, signal_label: SignalLabel) -> None:
        """
        Initialize with group_name and signal_label.
        :param group_name: Group name
        :type group_name: GroupName
        :param signal_label: Signal label
        :type signal_label: SignalLabel
        """
        self.group_name: GroupName = group_name
        self.signal_label: SignalLabel = signal_label

class Group:

    def __init__(self, name: str):
        self.name: GroupName = GroupName(name)
        self.signals: dict[SignalLabel, SignalRecord] = {}

    def add_data(self, label: str, data: Any, *, tick_name: str = None) -> None:
        """
        Add a single data variable with a label and store it to the default group.
        Each call to this function will increase the sample time by one.
        A new TimeTick object is created for this time sample.
        If time is manually paused, the new TimeTick object overwrites the previous TimeTick for time.current_time.
        :param label: Label of the variable.
        :type label: str
        :param data: Value of the variable.
        :param tick_name: Name parameter of corresponding TimeTick object, defaults to None
        :type tick_name: str, optional
        """
        signal_label = SignalLabel(label)
        signal_value = SignalValue(data)
        if signal_label not in self.signals:
            self.signals[signal_label] = {}
        current_time = time.current_time
        new_time_tick = add_new_time_tick(current_time, tick_name)
        self.signals[label][new_time_tick] = signal_value
        time.tick()

    def add_data_multi(self, data_dict: dict, *, tick_name: str = None) -> None:
        """
        Add multiple data with the dict format {label: var} and store them to the default group.
        This function will pause the sampling time, add all data, and then resume the sampling time;
        so the change of data will be stored and saved in one sample time.
        A new TimeTick object is created for this time sample.
        If time is manually paused, the new TimeTick object overwrites the previous TimeTick for time.current_time.
        :param data_dict: Dictionary of variable, with labels as keys and data as values.
        :type data_dict: dict
        :param tick_name: Name parameter of corresponding TimeTick object, defaults to None
        :type tick_name: str, optional
        """
        time.pause()
        for label, data in data_dict.items():
            self.add_data(label, data)
        time.resume()

    def plot(self, gui_engine: GuiEngine = GuiEngine.default) -> None:
        """
        Plot all logged variables in this group with the selected GUI engine. Currently the default and only engine is 'pyplot'.
        :param gui_engine: the selected engine for plotting the data
        :return: None
        """
        plot_manager.plot_manager(gui_engine, self.name)
