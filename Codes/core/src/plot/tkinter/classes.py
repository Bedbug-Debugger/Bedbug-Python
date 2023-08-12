from __future__ import annotations
import tkinter as tk

from .. import plot_utility
from ..const import (
    Color,
    SPACE,
    HARD_SPLIT,
    SOFT_SPLIT,
    DOT,
    FONT_BOLD,
    FONT_NORMAL
)
from ...models.wrappers import (
    GroupSignalPair,
    TimeTick,
    TkChar
)
from ... import bedbug as bd

def change(element, param: str, value) -> None:
	if element[param] != value:
		element[param] = value

class TkPlotterWindow:
	"""
	Wrapper class for managing the main tk.Tk window.
	"""

	def __init__(self, name: str, signals: list[GroupSignalPair]) -> None:
		"""
		Initialize a TkPlotterWindow object.
		:param name: A string for identifying this object.
		:type name: str
		:param signals: List of signals to plot.
		:type signals: list[GroupSignalPair]
		"""
		self.name: str = name
		self.tk_element = tk.Tk()
		# Variables
		self.signals: list[GroupSignalPair] = signals
		self.num_of_signals: int = len(self.signals)
		self.time_ticks: list[TimeTick] = plot_utility.get_time_ticks(self.signals)
		self.num_of_time_ticks: int = len(self.time_ticks)
		self.num_of_lines: int = 8
		self.num_of_name_columns: int = 8
		self.num_of_plot_columns: int = 30
		self.tick_distance: int = 8
		self.first_line: int = 0
		self.first_col: int = 0
		self.line_data: list[list[TkChar]] = [None] * self.num_of_lines
		self.line_data_length: int = (self.num_of_time_ticks * (1 + self.tick_distance))
		# Subwidgets
		self.signal_name_frame = TkNameFrame(
			name='signal_name_frame',
			master=self,
			signals=self.signals
		)
		self.signal_plot_frame = TkPlotFrame(
			name='signal_plot_frame',
			master=self,
			signals=self.signals
		)
		# Event binding
		self.tk_element.bind('<Key-Left>', self.handle_event)
		self.tk_element.bind('<Key-Right>', self.handle_event)
		self.tk_element.bind('<Key-Up>', self.handle_event)
		self.tk_element.bind('<Key-Down>', self.handle_event)
		# Draw
		self.draw_screen()

	def handle_event(self, event: tk.Event) -> None:
		"""
		Handle a given event.
		:param event: tk event name.
		:type event: tk.Event
		"""
		refresh_screen = False
		line_change = False
		if event.keysym == 'Left':
			if self.first_col > 0:
				self.first_col -= 1
				refresh_screen = True
		elif event.keysym == 'Right':
			if self.first_col + self.num_of_plot_columns <= self.line_data_length:
				self.first_col += 1
				refresh_screen = True
		elif event.keysym == 'Up':
			# TODO
			line_change = True
			refresh_screen = True
		elif event.keysym == 'Down':
			# TODO
			line_change = True
			refresh_screen = True
		if refresh_screen:
			self.draw_screen(line_change=line_change)

	def draw_screen(self, *, line_change: bool = True) -> None:
		"""
		(Re)draw the whole screen.

		:param line_change: Whether write_line_data should be called, or not, defaults to True
		:type line_change: bool
		"""
		for line in range(self.num_of_lines):
			self.clear_line(line=line)
			signal_num = line + self.first_line
			if signal_num >= self.num_of_signals:
				continue
			if line_change:
				self.write_line_data(line=line, signal=self.signals[signal_num], time_ticks=self.time_ticks)
			self.draw_line(line=line, signal=self.signals[signal_num])

	def clear_line(self, *, line: int) -> None:
		"""
		Clear the name and plot in a line.
		:param line: Line number (0 is the top visible line).
		:type line: int
		"""
		# Name frame
		for col in range(self.num_of_name_columns):
			change(self.signal_name_frame.signal_lines[line][col], 'text', SPACE)
		# Plot frame
		for col in range(self.num_of_plot_columns):
			change(self.signal_plot_frame.signal_lines[line][col], 'text', SPACE)

	def write_line_data(self, *, line: int, signal: GroupSignalPair, time_ticks: list[TimeTick]) -> None:
		"""
		Internally store the characters to display in a line.
		draw_line(...) decides which portion of this written data to show.
		:param line: Line number (0 is the top visible line).
		:type line: int
		:param signal: A GroupSignalPair, denoting the signal to draw in this line.
		:type signal: GroupSignalPair
		:param time_ticks: List of all TimeTick's in this bedbug session.
		:type time_ticks: list[TimeTick]
		"""
		self.line_data[line] = []
		value: str = ""
		for tick in time_ticks:
			group_name = signal.group_name
			signal_label = signal.signal_label
			group = bd.get_group(group_name.name)
			record = group.signals[signal_label]
			new_value = False
			if tick in record.record:
				self.line_data[line].append(TkChar(HARD_SPLIT, special=True))
				value = record.record[tick].value
				new_value = True
			else:
				self.line_data[line].append(TkChar(SOFT_SPLIT, special=True))
			value_is_long = (len(value) > self.tick_distance)
			for data_col in range(self.tick_distance):
				if value_is_long:
					if data_col < self.tick_distance - 3:
						self.line_data[line].append(TkChar(value[data_col], new_value=new_value))
					else:
						self.line_data[line].append(TkChar(DOT, new_value=new_value))
				else:
					if data_col < len(value):
						self.line_data[line].append(TkChar(value[data_col], new_value=new_value))
					else:
						self.line_data[line].append(TkChar(SPACE, new_value=new_value))
	
	def draw_line(self, *, line: int, signal: GroupSignalPair) -> None:
		"""
		Draw the name and plot in a line.
		:param line: Line number (0 is the top visible line).
		:type line: int
		:param signal: A GroupSignalPair, denoting the signal to draw in this line.
		:type signal: GroupSignalPair
		"""
		# Name frame
		label = plot_utility.get_signal_full_label(group_name=signal.group_name, signal_label=signal.signal_label)
		self.signal_name_frame.write_label(row=line, label=label)
		# Plot frame
		data = self.line_data[line]
		for col in range(self.num_of_plot_columns):
			# data_col is changed by going left and right in the screen, which changes self.first_col.
			data_col = self.first_col + col
			if data_col >= len(data):
				break
			self.signal_plot_frame.write_label(row=line, col=col, tkchar=data[data_col])
	
class TkFrame:
	"""
	Base class for managing tk.Frame widgets.
	"""
	def __init__(
			self,
			name: str,
			master: TkFrame | TkPlotterWindow,
			handled_events: list[str] = []
	) -> None:
		"""

		:param name: A string for identifying this object.
		:type name: str
		:param master: The master to connect the underlying tk.Frame to its tk_element.
		:type master: TkFrame | TkPlotterWindow
		:param handled_events: List of events to handle as a list of tk event names, defaults to []
		:type handled_events: list[str], optional
		"""
		self.name: str = name
		self.master: TkFrame | TkPlotterWindow = master
		self.tk_element: tk.Frame = None
		for handled_event in handled_events:
			self.tk_element.bind(handled_event, self.handle_event)
		# Define tk element
		self.define_tk_element()
		
	def define_tk_element(self) -> None:
		"""
		Define the Frame widget which this class relies on. Base function to inherit.
		"""
		self.tk_element = tk.Frame(
			master=self.master.tk_element
		)
		self.tk_element.pack()

	def handle_event(self, event: tk.Event) -> None:
		"""
		Handle a given event. Base function to inherit.
		:param event: tk event name.
		:type event: tk.Event
		"""
		pass

class TkNameFrame(TkFrame):
	"""
	Wrapper class for the signal name frame. This class inherits from TkFrame.
	"""	
	def __init__(
			self,
	    	name: str,
			master: TkPlotterWindow,
			signals: list[GroupSignalPair],
	    	handled_events: list[str] = []
	) -> None:
		"""
		Initialize a TkNameFrame object.
		:param name: A string for identifying this object.
		:type name: str
		:param master: The master to connect the underlying tk.Frame to its tk_element.
		:type master: TkPlotterWindow
		:param signals: List of signals to plot.
		:type signals: list[GroupSignalPair]
		:param num_of_lines: Number of lines to display, defaults to TkPlotterWindow.num_of_lines
		:type num_of_lines: int, optional
		:param handled_events: List of events to handle as a list of tk event names, defaults to []
		:type handled_events: list[str], optional
		"""
		self.name: str = name
		self.master: TkPlotterWindow = master
		self.tk_element: tk.Frame = None
		# Variables
		self.signals: list[GroupSignalPair] = signals
		self.num_of_signals: int = len(signals)
		self.num_of_lines: int = master.num_of_lines
		self.num_of_columns: int = master.num_of_name_columns
		self.bg: str = Color.NAME_INACTIVE_BG.value
		self.fg: str = Color.NAME_FG.value
		self.font: str = FONT_NORMAL
		# Define tk element
		self.define_tk_element()
		# Subwidgets
		self.signal_lines: list[list[tk.Label]] = [None] * self.num_of_lines
		for row in range(self.num_of_lines):
			self.signal_lines[row] = [None] * self.num_of_columns
			for col in range(self.num_of_columns):
				self.signal_lines[row][col] = tk.Label(
					master=self.tk_element,
					text=SPACE,
					bg=self.bg,
					fg=self.fg,
					font=self.font
				)
				self.signal_lines[row][col].grid(row=row, column=col)
		for handled_event in handled_events:
			self.tk_element.bind(handled_event, self.handle_event)

	
	def define_tk_element(self) -> None:
		"""
		Define the Frame widget which this class relies on.
		"""
		self.tk_element = tk.Frame(
			master=self.master.tk_element
			# bg=self.bg
			# width=100,
			# height=100
		)
		self.tk_element.grid(row=0, column=0)
	
	def write_label(self, *, row: int, label: str) -> None:
		for col in range(self.master.num_of_name_columns):
			if col < len(label):
				change(self.signal_lines[row][col], 'text', label[col])
			change(self.signal_lines[row][col], 'bg', Color.NAME_ACTIVE_BG.value)

class TkPlotFrame(TkFrame):
	"""
	Wrapper class for the plot frame. This class inherits from TkFrame.
	"""
	def __init__(
			self,
	    	name: str,
			master: TkPlotterWindow,
			signals: list[GroupSignalPair],
	    	handled_events: list[str] = []
	) -> None:
		"""
		Initialize a TkPlotFrame object.
		:param name: A string for identifying this object.
		:type name: str
		:param master: The master to connect the underlying tk.Frame to its tk_element.
		:type master: TkPlotterWindow
		:param signals: List of signals to plot.
		:type signals: list[GroupSignalPair]
		:param num_of_lines: Number of lines to display, defaults to TkPlotterWindow.num_of_lines
		:type num_of_lines: int, optional
		:param num_of_columns: Number of plot columns to display, defaults to TkPlotterWindow.num_of_plot_columns
		:type num_of_columns: int, optional
		:param handled_events: List of events to handle as a list of tk event names, defaults to []
		:type handled_events: list[str], optional
		"""
		self.name: str = name
		self.master: TkPlotterWindow = master
		self.tk_element: tk.Frame = None
		# Variables
		self.signals: list[GroupSignalPair] = signals
		self.num_of_signals: int = len(signals)
		self.num_of_lines: int = master.num_of_lines
		self.num_of_columns: int = master.num_of_plot_columns
		self.fg: str = Color.PLOT_FG_NORMAL.value
		self.font: str = FONT_NORMAL
		self.time_ticks: list[TimeTick] = None
		# Define tk element
		self.define_tk_element()
		# Subwidgets
		self.signal_lines: list[list[tk.Label]] = [None] * self.num_of_lines
		for row in range(self.num_of_lines):
			self.signal_lines[row] = [None] * self.num_of_columns
			for col in range(self.num_of_columns):
				self.signal_lines[row][col] = tk.Label(
					master=self.tk_element,
					text=SPACE,
					bg=Color.PLOT_INACTIVE_BG.value,
					fg=self.fg,
					font=self.font
				)
				self.signal_lines[row][col].grid(row=row, column=col)
		# Event binding
		for handled_event in handled_events:
			self.tk_element.bind(handled_event, self.handle_event)

	
	def define_tk_element(self) -> None:
		"""
		Define the Frame widget which this class relies on.
		"""
		self.tk_element = tk.Frame(
			master=self.master.tk_element
		)
		self.tk_element.grid(row=0, column=1)

	def write_label(self, *, row: int, col: int, tkchar: TkChar) -> None:
		label = self.signal_lines[row][col]
		change(label, 'text', tkchar.char)
		# bg
		if tkchar.new_value:
			change(label, 'bg', Color.PLOT_ACTIVE_BG.value)
		else:
			change(label, 'bg', Color.PLOT_INACTIVE_BG.value)
		# fg
		if tkchar.special:
			change(label, 'fg', Color.PLOT_FG_SPECIAL.value)
		else:
			change(label, 'fg', Color.PLOT_FG_NORMAL.value)
		# font
		if tkchar.special:
			change(label, 'font', FONT_BOLD)
		else:
			change(label, 'font', FONT_NORMAL)



TK_GUI: TkPlotterWindow = None
