from time_manager import time

class Group:

    def __init__(self, name: str):
        self.name: str = name
        self.vars: dict[str, list] = {}

    def add_data(self, label: str, data) -> None:
        if label not in self.vars:
            self.vars[label] = []
        self.vars[label].append((time.current_time, data))
        time.tick()
    
    def add_data(self, data_dict: dict) -> None:
        time.pause()
        for label, data in data_dict.items():
            self.add_data(label, data)
        time.resume()
        
    def plot(self) -> None:
        pass
