"""
The main file of bedbug package.

You should import this file to use the package.
"""

import json

from .gui.gui_engines import GuiEngine
from .models import const
from .errors.group_errors import GroupNotFoundError, GroupAlreadyExistsError
from .models.group import Group
from .models import wrappers
from .gui import plot_manager
from .models import time_manager
from .models import wrappers

_groups: dict[wrappers.GroupName, Group] = {
	wrappers.GroupName(const.DEFAULT_GROUP_NAME): Group(const.DEFAULT_GROUP_NAME)
}
"""
Global variable which stores different groups and saves them for later uses.
The default group name is 'default_group_name' and all of the functions in this file store the data in this group. 
Groups are responsible for managing and organizing the variables.
"""


def create_group(name: str) -> Group:
	"""
	Create a group and return it to organize variables.
	See 'models.group.Group' for more details about groups.
	:raises GroupAlreadyExistsError: if there is a group with the same name.
	:param name: name of the group
	:return: an instance of the Group class
	"""
	group_name = wrappers.GroupName(name)
	if group_name in _groups:
		raise GroupAlreadyExistsError(name)
	group = Group(name)
	_groups[group_name] = group
	return group


def get_group(name: str) -> Group:
	"""
	Return an instance of an already created group.
	:raises GroupNotFoundError: if no group with the given name exists;
	groups should be created using the create_group function.
	:param name: target group name that you want to get
	:return: the created instance of Group class
	"""
	group_name = wrappers.GroupName(name)
	if group_name not in _groups:
		raise GroupNotFoundError(name)
	return _groups[group_name]


def add_data(label: str, data, *, tick_name: str = None) -> None:
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
	get_group(const.DEFAULT_GROUP_NAME).add_data(label, data, tick_name=tick_name)


def add_data_multi(data_dict: dict, *, tick_name: str = None) -> None:
	"""
	Add multiple data with the dict format {label: var} and store them to the default group.
	This function will pause the sampling time, add all data, and then resume the sampling time;
	so the change of data will be stored and saved in one sample time.
	A new TimeTick object is created for this time sample.
	If time is manually paused, the new TimeTick object overwrites the previous TimeTick for time.current_time.
	:param data_dict: Dictionary of variables, with labels as keys and data as values.
	:type data_dict: dict
	:param tick_name: Name parameter of corresponding TimeTick object, defaults to None
	:type tick_name: str, optional
	"""
	get_group(const.DEFAULT_GROUP_NAME).add_data_multi(data_dict, tick_name=tick_name)


def plot(gui_engine: GuiEngine = GuiEngine.default) -> None:
	"""
	Plot all logged variables in all groups with the selected GUI engine.
	Currently, the default and only engine is 'pyplot'.
	:param gui_engine: the selected engine for plotting the data
	:return: None
	"""
	plot_manager.plot_manager(gui_engine)

def _plot(group: Group, gui_engine: GuiEngine = GuiEngine.default) -> None:
	plot_manager.plot_manager(gui_engine=gui_engine, plot_group=group.name.name)


def dump_json(filename: str) -> None:
	JSON = {'timetick': [], 'groups': {}}
	# Add ticks
	for tick_int, time_tick in time_manager.time_ticks_from_time.items():
		JSON['timetick'].append([tick_int, time_tick.tick_name])
	# Add data
	for group_name, group in _groups.items():
		JSON['groups'][group_name.name] = {}
		for signal_label, record in group.signals.items():
			JSON['groups'][group_name.name][signal_label.label] = []
			for time_tick, signal_value in record.record.items():
				JSON['groups'][group_name.name][signal_label.label].append([time_tick.time, signal_value.value])
	# Write
	json.dump(JSON, filename)


def import_json(filename: str) -> None:
	# Read
	JSON = json.load(filename)
	# Get ticks
	for tick in JSON['timetick']:
		tick_int = tick[0]
		tick_name = tick[1]
		time_tick = wrappers.TimeTick(tick_int, tick_name)
		time_manager.time_ticks_from_time[tick_int] = time_tick
	# Get data
	for group_name_str in JSON['groups']:
		group = Group(group_name_str)
		group_name = wrappers.GroupName(group_name_str)
		for signal_label_str in JSON['groups'][group_name_str]:
			signal_label = wrappers.SignalLabel(signal_label_str)
			signal_record = wrappers.SignalRecord()
			for tick in JSON['groups'][group_name_str][signal_label_str]:
				tick_int = tick[0]
				value = tick[1]
				time_tick = time_manager.time_ticks_from_time[tick_int]
				signal_value = wrappers.SignalValue(value)
				signal_record[time_tick] = signal_value
			group.signals[signal_label] = signal_record
		_groups[group_name] = group
