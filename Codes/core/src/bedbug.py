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


def add_data(data, label: str) -> None:
    get_group(const.DEFAULT_GROUP_NAME).add_data(data, label)


def plot() -> None:
    pass


def dump_json(filename: str) -> None:
    pass


def import_json(filename: str) -> None:
    pass
