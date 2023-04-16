"""
The main file of bedbug package.

should import this file to use the package
"""

from overload import overload
from . import const
from .errors.group_errors import GroupNotFoundError, GroupAlreadyExistsError
from .models.group import Group
from .models.time_manager import time
from gui_engines import GuiEngine

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
    :raises GroupNotFoundError: if there is not any created group with the name given.
    :param name: target group name that you want to get
    :return: the created instance of Group class
    """
    if name not in _groups:
        raise GroupNotFoundError
    return _groups[name]


@overload
def add_data(data_dict: dict) -> None:
    """
    Add data as a dict with this format: {"label": var} and store it to the default group.
    This function will pause the sampling time, add all data, then resumes the sampling time;
    so the change of data will be stored and saved in one sample time.
    :param data_dict: is a dictionary of variables which you could add many data at once.
    :return: None
    """
    get_group(const.DEFAULT_GROUP_NAME).add_data(data_dict)


@add_data.add
def add_data(label: str, data) -> None:
    """
    Add a single data variable with a label and store it to the default group.
    Each call to this function will increase the sample time by one.
    :param label: variable label name
    :param data: value of the variable
    :return: None
    """
    get_group(const.DEFAULT_GROUP_NAME).add_data(label, data)


def plot(gui_engine: GuiEngine = GuiEngine.PyPlot) -> None:
    """
    Plot all the groups with the selected GUI engine. currently the default and only engine is 'pyplot'
    :param gui_engine: the selected engine for plotting the data
    :return: None
    """
    if gui_engine == GuiEngine.PyPlot:
        pass


def dump_json(filename: str) -> None:
    pass


def import_json(filename: str) -> None:
    pass
