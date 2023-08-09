from __future__ import annotations
from typing import Union
import tkinter as tk

class TkPlotterWindow:
    
	def __init__(self, name: str):
		self.name: str = name
		self.tk_element = tk.Tk()
		# Variables
		self.num_of_signals: int = None
		# Subwidgets
		self.signal_name_frame = TkFrame(name='signal_name_frame', master=self.tk_element)
		self.signal_plot_frame = TkPlotFrame(name='signal_plot_frame', master=self.tk_element)
		# Event binding
		self.tk_element.bind('<Key-Left>', self.handle_event)
		self.tk_element.bind('<Key-Right>', self.handle_event)
		self.tk_element.bind('<Key-Up>', self.handle_event)
		self.tk_element.bind('<Key-Down>', self.handle_event)

	def handle_event(self, event):
		pass

class TkFrame:

	def __init__(self, name: str, master: Union[TkFrame, TkPlotterWindow], handled_events: list[str] = []):
		self.name: str = name
		self.master: Union[TkFrame, TkPlotterWindow] = master
		self.tk_element: tk.Frame = None
		self.define_tk_element()
		for handled_event in handled_events:
			self.tk_element.bind(handled_event, self.handle_event)
	
	def define_tk_element(self):
		self.tk_element = tk.Frame(
			master=self.master
		)
		self.tk_element.pack()

	def handle_event(self, event):
		pass

class TkPlotFrame(TkFrame):

	def define_tk_element(self):
		self.tk_element = tk.Frame(
			master=self.master,
			bg='#003366',
			width=100,
			height=100
		)
		self.tk_element.pack()



TK_GUI: TkPlotterWindow = None
