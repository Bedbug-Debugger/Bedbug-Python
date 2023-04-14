class GroupNotFoundError(KeyError):
    def __init__(self, key):
        self.message = f"GroupNotFoundError: group {key} does not exists."

    def __str__(self):
        return self.message


class GroupAlreadyExistsError(Exception):
    def __init__(self, name: str):
        self.message = f"GroupAlreadyExistsError: group {name} already exists."
