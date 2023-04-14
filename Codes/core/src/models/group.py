class Group:

    def __init__(self, name: str):
        self.name: str = name
        self.vars: dict[str, list] = {}

    def add_data(self, data, label: str) -> None:
        if label not in self.vars:
            self.vars[label] = []
        self.vars[label].append(data)

    def plot(self) -> None:
        pass
