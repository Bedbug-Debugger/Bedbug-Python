from .. import const

DEFAULT_TIME_MANAGER_NAME = "default_time_manager_name"

class TimeManager:
    
	def __init__(self, name: str = const.DEFAULT_TIME_MANAGER_NAME):
		self.name: str = name
		self.current_time: int = 0
		self.paused: bool = False
	
	def tick(self) -> None:
		if not self.paused:
			self.current_time += 1
	
	def pause(self) -> None:
		self.paused = True
	
	def resume(self) -> None:
		self.paused = False
		# For correct behavior after a pause, a tick is needed.
		# Example:
		#	import bedbug as bd
		#	a, b = 0, 0
		#	bd.time.pause()
		#	bd.add_data("a", a)		# adds (0, a), keeps current_time = 0
		#	bd.add_data("b", b)		# adds (0, b), keeps current_time = 0
		#	bd.time.resume()		# lets current_time = 1
		#	a = 12
		#	bd.add_data("a", a)		# adds (1, a) since current_time is 1, then lets current_time = 2
		self.tick()


time = TimeManager()