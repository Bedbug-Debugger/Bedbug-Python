from __future__ import annotations
from typing import Union
import tkinter as tk

class TkWindow:
    
	def __init__(self, name: str):
		self.name: str = name
		self.tk_element = tk.Tk()
		self.signal_name_frame = TkFrame(name='signal_name_frame', master=self.tk_element)
		self.signal_plot_frame = TkFrame(name='signal_plot_frame', master=self.tk_element)
		self.tk_element.bind('<Button-1>', self.handle_event)
	
	def handle_event(self):
		print('Gotcha!')

class TkFrame:

	def __init__(self, name: str, master: Union[TkFrame, TkWindow], handled_events: list[str] = []):
		self.name: str = name
		self.master: Union[TkFrame, TkWindow] = master
		self.tk_element = tk.Frame(
			master=self.master
		)
		for handled_event in handled_events:
			self.tk_element.bind(handled_event, self.handle_event)
	
	def handle_event(self):
		pass



TK_GUI: TkWindow = None
