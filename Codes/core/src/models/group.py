class Group:

    def __init__(self, name: str):
        self.name: str = name
        self.vars: dict[str, list] = {}

    def add_data(self, data, label: str) -> None:
        self.vars[label].append(data)
