"""
The main file of bedbug package.

You should import this file to use the package.
# TODO: add documentation for fundamental concepts.
"""

from .gui_engines import GuiEngine
from . import const
from .errors.group_errors import GroupNotFoundError, GroupAlreadyExistsError
from .models.group import Group
from .models.time_manager import time
from .plot import plot_manager

_groups: dict[str, Group] = {
    const.DEFAULT_GROUP_NAME: Group(const.DEFAULT_GROUP_NAME)
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
    if name in _groups:
        raise GroupAlreadyExistsError(name)
    group = Group(name)
    _groups[name] = group
    return group


def get_group(name: str) -> Group:
    """
    Return an instance of an already created group.
    :raises GroupNotFoundError: if no group with the given name exists;
    groups should be created using the create_group function.
    :param name: target group name that you want to get
    :return: the created instance of Group class
    """
    if name not in _groups:
        raise GroupNotFoundError
    return _groups[name]


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
    plot_manager.plot_manager(gui_engine, None)


def dump_json(filename: str) -> None:
    pass


def import_json(filename: str) -> None:
    pass
