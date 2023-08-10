from __future__ import annotations
import tkinter as tk

class TkPlotterWindow:
    
	num_of_signals_in_screen: int = 8

	def __init__(self, name: str, signals: list[tuple[str, str]]):
		self.name: str = name
		self.tk_element = tk.Tk()
		# Variables
		self.signals: list[tuple[str, str]] = signals
		# Subwidgets
		self.signal_name_frame = TkFrame(
			name='signal_name_frame',
			master=self.tk_element,
			# signals=self.signals
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

	def handle_event(self, event):
		pass

class TkFrame:

	def __init__(
			self,
			name: str,
			master: TkFrame | TkPlotterWindow,
			handled_events: list[str] = []
	):
		self.name: str = name
		self.master: TkFrame | TkPlotterWindow = master
		self.tk_element: tk.Frame = None
		for handled_event in handled_events:
			self.tk_element.bind(handled_event, self.handle_event)
		# Define tk element
		self.define_tk_element()
		
	def define_tk_element(self):
		self.tk_element = tk.Frame(
			master=self.master
		)
		self.tk_element.pack()

	def handle_event(self, event):
		pass

class TkPlotFrame(TkFrame):
	
	def __init__(
			self,
	    	name: str,
			master: TkFrame | TkPlotterWindow,
			signals: list[tuple[str, str]],
			num_of_lines: float = TkPlotterWindow.num_of_signals_in_screen,
	    	handled_events: list[str] = []
	):
		self.name: str = name
		self.master: TkFrame | TkPlotterWindow = master
		self.tk_element: tk.Frame = None
		# Variables
		self.signals: signals
		self.num_of_signals: int = len(signals)
		self.num_of_lines: float = num_of_lines
		self.bg: str = '#003366'
		self.fg: str = '#ffffff'
		self.font: str = 'Courier'
		# Define tk element
		self.define_tk_element()
		# Subwidgets
		self.signal_lines: list[tk.Frame] = [None] * self.num_of_lines
		for signal_num in range(self.num_of_lines):
			self.signal_lines[signal_num] = tk.Label(
				master=self.tk_element,
				text=f'{signal_num=}',
				bg=self.bg,
				fg=self.fg,
				font=self.font
			)
			# self.tk_element.grid(row=num_of_lines, column=1)
			# self.signal_lines[signal_num].pack()
			self.signal_lines[signal_num].grid(row=signal_num, column=1)
		# Event binding
		for handled_event in handled_events:
			self.tk_element.bind(handled_event, self.handle_event)

	
	def define_tk_element(self):
		self.tk_element = tk.Frame(
			master=self.master,
			bg=self.bg,
			width=100,
			height=100
		)
		self.tk_element.pack()



TK_GUI: TkPlotterWindow = None
