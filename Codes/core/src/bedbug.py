from models.group import Group
import const
from errors.group_not_found_error import GroupNotFoundError

_groups: dict[str, Group] = {}


def create_group(name: str) -> Group:
    group = Group(name)
    _groups[name] = group
    return group


def get_group(name: str) -> Group:
    if name not in _groups:
        if name == const.DEFAULT_GROUP_NAME:
            return create_group(const.DEFAULT_GROUP_NAME)
        raise GroupNotFoundError
    return _groups[name]


def add_data(var, label: str, group: str = const.DEFAULT_GROUP_NAME) -> None:
    get_group(group).add_data(var, label)


def plot() -> None:
    pass


def dump_json(filename: str) -> None:
    pass


def import_json(filename: str) -> None:
    pass
