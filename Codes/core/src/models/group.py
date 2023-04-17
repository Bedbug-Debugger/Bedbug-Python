from .time_manager import time


class Group:

    def __init__(self, name: str):
        self.name: str = name
        self.vars: dict[str, dict] = {}

    def add_data(self, label: str, data) -> None:
        """
        Add a single data variable with a label and store it to the default group.
        Each call to this function will increase the sample time by one.
        :param label: the label of the variable
        :param data: the value of the variable
        :return: None
        """
        if label not in self.vars:
            self.vars[label] = {}
        self.vars[label][time.current_time] = data
        time.tick()

    def add_data_multi(self, data_dict: dict) -> None:
        """
        Add multiple data with the dict format {label: var} and store them to the default group.
        This function will pause the sampling time, add all data, and then resume the sampling time;
        so the change of data will be stored and saved in one sample time.
        :param data_dict: a dictionary of variables, with labels as keys and data as values
        :return: None
        """
        time.pause()
        for label, data in data_dict.items():
            self.add_data(label, data)
        time.resume()

    def plot(self) -> None:
        pass
