from overload import overload
from . import const
from .errors.group_errors import GroupNotFoundError, GroupAlreadyExistsError
from .models.group import Group
from .models.time_manager import time

_groups: dict[str, Group] = {
    const.DEFAULT_GROUP_NAME: Group(const.DEFAULT_GROUP_NAME)
}


def create_group(name: str) -> Group:
    if name in _groups:
        raise GroupAlreadyExistsError(name)
    group = Group(name)
    _groups[name] = group
    return group


def get_group(name: str) -> Group:
    if name not in _groups:
        raise GroupNotFoundError
    return _groups[name]


@overload
def add_data(data_dict: dict) -> None:
    get_group(const.DEFAULT_GROUP_NAME).add_data(data_dict)


@add_data.add
def add_data(label: str, data) -> None:
    get_group(const.DEFAULT_GROUP_NAME).add_data(label, data)


def plot() -> None:
    pass


def dump_json(filename: str) -> None:
    pass


def import_json(filename: str) -> None:
    pass
