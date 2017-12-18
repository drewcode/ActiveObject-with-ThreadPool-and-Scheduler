from multiprocessing import Pool, Lock
from time import time

locks = []


class fooclass:
	def __init__(self):
		self.var = 5

	def foo(self, i):
		ans = 0
		for j in range(1,1000000):
			ans += self.var * (i+j) ** 172.384 ** (1 / i**2.3242)
		return ans


class wrapper:
	def __init__(self, obj):
		self.obj = obj


	def __getattr__(self, name):
		def closure(*args):
			return Scheduler.apply_as(getattr(self.obj, name), *args)
		return closure


class Scheduler:
	@staticmethod
	def __init__(n):
		Scheduler.pool = Pool(processes = (n-1))
		Scheduler.pool.apply_async()
		Scheduler.counter = 0

	@staticmethod
	def apply_as(fn, *args):
		return Scheduler.pool.apply_async(fn, args)

	@staticmethod
	def get_counter():
		Scheduler.counter += 1
		return Scheduler.counter 


if __name__ == '__main__':

	
	Scheduler(4)


	wrapper(fooclass()).foo(60)

