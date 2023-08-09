from __future__ import annotations
from typing import Union
import tkinter as tk

class TkPlotterWindow:
    
	def __init__(self, name: str):
		self.name: str = name
		self.tk_element = tk.Tk()
		# Subwidgets
		self.signal_name_frame = TkFrame(name='signal_name_frame', master=self.tk_element)
		self.signal_plot_frame = TkFrame(name='signal_plot_frame', master=self.tk_element)
		# Event binding
		self.tk_element.bind('<Key-Left>', self.handle_event)
		self.tk_element.bind('<Key-Right>', self.handle_event)
		# signal_name_frame
		self.signal_name_frame.tk_element.pack()
		self.label1 = tk.Label(master=self.signal_name_frame.tk_element, text="0")
		self.label1.pack()

	def handle_event(self, event):
		print(f"{event.keysym=}")
		num = int(self.label1['text'])
		if event.keysym == 'Left':
			num -= 1
		elif event.keysym == 'Right':
			num += 1
		self.label1['text'] = f"{num}"

class TkFrame:

	def __init__(self, name: str, master: Union[TkFrame, TkPlotterWindow], handled_events: list[str] = []):
		self.name: str = name
		self.master: Union[TkFrame, TkPlotterWindow] = master
		self.tk_element = tk.Frame(
			master=self.master
		)
		for handled_event in handled_events:
			self.tk_element.bind(handled_event, self.handle_event)
	
	def handle_event(self):
		pass



TK_GUI: TkPlotterWindow = None
