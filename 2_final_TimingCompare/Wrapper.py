class wrapper:
	def __init__(self, obj, scheduler):
		self.obj = obj
		self.scheduler = scheduler

	def __getattr__(self, name):
		def closure(*args):
			return self.scheduler.apply(getattr(self.obj, name), *args)
		return closure