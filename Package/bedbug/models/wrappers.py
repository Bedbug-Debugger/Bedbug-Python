from __future__ import annotations
from typing import (
    Any, Iterator
)
from dataclasses import dataclass


@dataclass(eq=True, frozen=True, order=True)
class TimeTick:
	"""
	A wrapper class for (time, name of time tick).
	"""
	time: int
	tick_name: str

@dataclass(eq=True, frozen=True, order=True)
class SignalLabel:
	"""
	A wrapper class for signal labels.
	"""
	label: str

# @dataclass()
# class SignalValue:
# 	"""
# 	A wrapper class for signal values.
# 	"""
# 	def __init__(self, value: Any) -> None:
# 		"""
# 		Initialize with a value, which is stored as str.
# 		:param value: Signal value
# 		:type value: Any
# 		"""
# 		self.value: str = str(value)

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

# @dataclass()
# class SignalRecord:
# 	"""
# 	A wrapper class for dictionary of TimeTick's and corresponding SignalValue's.
# 	"""
# 	record: dict[TimeTick, SignalValue] = field(default_factory=dict)

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

@dataclass(eq=True, frozen=True, order=True)
class GroupName:
	"""
	A wrapper class for group names.
	"""
	name: str

@dataclass(eq=True, frozen=True, order=True)
class GroupSignalPair:
	"""
	A wrapper class for (group name, signal label).
	"""
	group_name: GroupName
	signal_label: SignalLabel

@dataclass(eq=True, frozen=True)
class TkChar:
	char: str
	special: bool = False
	new_value: bool = False
