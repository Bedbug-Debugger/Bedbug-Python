from __future__ import annotations
import tkinter as tk

from ...models.group import GroupSignalPair
from ...models.time_manager import TimeTick

class TkPlotterWindow:
	"""
	Wrapper class for managing the main tk.Tk window.
	"""
	num_of_lines: int = 8
	num_of_plot_columns: int = 30

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
		# Subwidgets
		self.signal_name_frame = TkNameFrame(
			name='signal_name_frame',
			master=self.tk_element,
			signals=self.signals
		)
		self.signal_plot_frame = TkPlotFrame(
			name='signal_plot_frame',
			master=self.tk_element,
			signals=self.signals
		)
		# Event binding
		self.tk_element.bind('<Key-Left>', self.handle_event)
		self.tk_element.bind('<Key-Right>', self.handle_event)
		self.tk_element.bind('<Key-Up>', self.handle_event)
		self.tk_element.bind('<Key-Down>', self.handle_event)

	def handle_event(self, event: tk.Event) -> None:
		"""
		Handle a given event.
		:param event: tk event name.
		:type event: tk.Event
		"""
		pass

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
		:param master: The tk master to connect the underlying tk.Frame to.
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
			master=self.master
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
			num_of_lines: int = TkPlotterWindow.num_of_lines,
	    	handled_events: list[str] = []
	) -> None:
		"""
		Initialize a TkNameFrame object.
		:param name: A string for identifying this object.
		:type name: str
		:param master: The tk master to connect the underlying tk.Frame to.
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
		self.num_of_lines: int = num_of_lines
		self.bg: str = '#EEEEEE'
		self.fg: str = '#000000'
		self.font: str = 'Courier'
		# Define tk element
		self.define_tk_element()
		# Subwidgets
		self.signal_lines: list[tk.Label] = [None] * self.num_of_lines
		for signal_num in range(self.num_of_lines):
			self.signal_lines[signal_num] = tk.Label(
				master=self.tk_element,
				text=f'{signal_num=}',
				bg=self.bg,
				fg=self.fg,
				font=self.font
			)
			self.signal_lines[signal_num].grid(row=signal_num, column=0)
		# Event binding
		for handled_event in handled_events:
			self.tk_element.bind(handled_event, self.handle_event)

	
	def define_tk_element(self) -> None:
		"""
		Define the Frame widget which this class relies on.
		"""
		self.tk_element = tk.Frame(
			master=self.master
			# bg=self.bg
			# width=100,
			# height=100
		)
		self.tk_element.grid(row=0, column=0)

class TkPlotFrame(TkFrame):
	"""
	Wrapper class for the plot frame. This class inherits from TkFrame.
	"""
	def __init__(
			self,
	    	name: str,
			master: TkPlotterWindow,
			signals: list[GroupSignalPair],
			num_of_lines: int = TkPlotterWindow.num_of_lines,
			num_of_columns: int = TkPlotterWindow.num_of_plot_columns,
	    	handled_events: list[str] = []
	) -> None:
		"""
		Initialize a TkPlotFrame object.
		:param name: A string for identifying this object.
		:type name: str
		:param master: The tk master to connect the underlying tk.Frame to.
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
		self.num_of_lines: int = num_of_lines
		self.num_of_columns: int = num_of_columns
		self.bg: str = '#003366'
		self.fg: str = '#ffffff'
		self.font: str = 'Courier'
		self.time_ticks: list[TimeTick] = None
		# Define tk element
		self.define_tk_element()
		# Subwidgets
		self.signal_lines: list[list[tk.Label]] = [None] * self.num_of_lines
		for row in range(self.num_of_lines):
			self.signal_lines[row] = [None] * self.num_of_columns
			for col in range(num_of_columns):
				self.signal_lines[row][col] = tk.Label(
					master=self.tk_element,
					text=f'X',
					bg=self.bg,
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
			master=self.master
		)
		self.tk_element.grid(row=0, column=1)

	def write_data(self, *, line: int, col_st: int = None, col_en: int = None) -> None:
		"""
		Write signal data in the plot frame.
		Writes in [col_st, col_en). Setting any of them to None lets the function truncate data in the plot value slot.
		:param line: Line number.
		:type line: int
		:param col_st: Column number to start, defaults to None
		:type col_st: int, optional
		:param col_en: Column number to end before, defaults to None
		:type col_en: int, optional
		"""
		pass



TK_GUI: TkPlotterWindow = None
