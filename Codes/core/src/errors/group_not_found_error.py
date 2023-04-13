class GroupNotFoundError(Exception):
    def __init__(self, key):
        self.message = f"GroupNotFoundError: group {key} does not exists."

    def __str__(self):
        return self.message
