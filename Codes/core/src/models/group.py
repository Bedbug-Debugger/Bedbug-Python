from .time_manager import time


class Group:

    def __init__(self, name: str):
        self.name: str = name
        self.vars: dict[str, dict] = {}

    def add_data(self, label: str, data) -> None:
        """
        Add a new data to the logged values of a variable.

        :param label: a name for the logged variable.
        :param data: the data to be logged for the variable.
        :return: None
        """
        if label not in self.vars:
            self.vars[label] = {}
        self.vars[label][time.current_time] = data
        time.tick()

    def add_data_multi(self, data_dict: dict) -> None:
        """
        Add new data to the logged values of one or more variables, all in one sampling time.

        :param data_dict: a dict consisting of variable names as keys, and data as values
        :return: None
        """
        time.pause()
        for label, data in data_dict.items():
            self.add_data(label, data)
        time.resume()

    # @overload
    # def add_data(self, data_dict: dict) -> None:
    #     self.add_data_dict(data_dict)
    #
    # @add_data.add
    # def add_data(self, label: str, data) -> None:
    #     self.add_data_single(label, data)

    def plot(self) -> None:
        pass
