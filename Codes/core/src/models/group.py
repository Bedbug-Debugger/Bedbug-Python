from typing import Any

from .time_manager import (
    TimeTick,
    time_ticks_from_time,
    time,
    add_new_time_tick
)
from .wrappers import (
    SignalLabel,
    SignalValue,
    SignalRecord,
    GroupName,
    GroupSignalPair
)
from ..gui_engines import GuiEngine
from ..plot import plot_manager


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
            self.signals[signal_label] = SignalRecord()
        current_time = time.current_time
        new_time_tick = add_new_time_tick(current_time, tick_name)
        self.signals[signal_label][new_time_tick] = signal_value
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
        plot_manager.plot_manager(gui_engine, self.name.name)
