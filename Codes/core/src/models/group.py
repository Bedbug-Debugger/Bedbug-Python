from overload import overload
from .time_manager import time

class Group:

    def __init__(self, name: str):
        self.name: str = name
        self.vars: dict[str, dict] = {}

    def add_data_single(self, label: str, data) -> None:
        if label not in self.vars:
            self.vars[label] = {}
        self.vars[label][time.current_time] = data
        time.tick()

    def add_data_dict(self, data_dict: dict) -> None:
        time.pause()
        for label, data in data_dict.items():
            self.add_data_single(label, data)
        time.resume()
    
    @overload
    def add_data(self, data_dict: dict) -> None:
        self.add_data_dict(data_dict)
    
    @add_data.add
    def add_data(self, label: str, data) -> None:
        self.add_data_single(label, data)
        
    def plot(self) -> None:
        pass
