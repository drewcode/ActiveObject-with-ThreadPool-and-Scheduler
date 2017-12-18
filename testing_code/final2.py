from multiprocessing import Pool
from time import time


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
			return Scheduler.apply(getattr(self.obj, name), *args)
		return closure


class Scheduler:
	@staticmethod
	def number_of_processes(n):
		Scheduler.pool = Pool(processes = n)

	@staticmethod
	def apply(fn, *args):
		return Scheduler.pool.apply_async(fn, args)


if __name__ == '__main__':

	
	Scheduler.number_of_processes(3)

	currtime2 = time()

	results = []
	for i in range(1,11):
		results.append(wrapper(fooclass()).foo(60*10*i))

	r2 = []
	for i in range(10):
		r2.append(results[i].get())
		print(str(r2))

	print (time() - currtime2)

	# futur = wrapper(fooclass()).foo(10)
	# print(futur.get())