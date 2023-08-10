from typing import (
    Any, Iterator
)

from .time_manager import TimeTick

class SignalLabel:
	"""
	A wrapper class for signal labels.
	"""
	def __init__(self, label: str) -> None:
		"""
		Initialize with a label.
		:param label: Signal label
		:type label: str
		"""
		self.label: str = label

class SignalValue:
	"""
	A wrapper class for signal values.
	"""
	def __init__(self, value: Any) -> None:
		"""
		Initialize with a value, which is stored as str.
		:param value: Signal value
		:type value: Any
		"""
		self.value: str = str(value)

class SignalRecord:
	"""
	A wrapper class for dictionary of TimeTick's and corresponding SignalValue's.
	"""
	def __init__(self) -> None:
		self.record: dict[TimeTick, SignalValue] = {}
	
	def __getitem__(self, time_tick: TimeTick) -> SignalValue:
		return self.record[time_tick]
	
	def __setitem__(self, time_tick: TimeTick, signal_value: SignalValue) -> None:
		self.record[time_tick] = signal_value

	def __iter__(self) -> Iterator[TimeTick]:
		return iter(self.record)
