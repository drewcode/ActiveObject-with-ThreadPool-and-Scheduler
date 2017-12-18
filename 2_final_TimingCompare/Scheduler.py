from multiprocessing import Pool

class scheduler:
	@staticmethod
	def number_of_processes(n):
		scheduler.pool = Pool(processes = n)

	@staticmethod
	def apply(fn, *args):
		return scheduler.pool.apply_async(fn, args)