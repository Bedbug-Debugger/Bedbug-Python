from models.group import Group

_groups: dict[str, Group] = {}


def create_group(name: str) -> None:
    group = Group(name)
    _groups[name] = group


def get_group(name: str) -> Group:
    pass


def add_var(var) -> None:
    pass


def plot() -> None:
    pass


def dump_json(filename: str) -> None:
    pass


def import_json(filename: str) -> None:
    pass
