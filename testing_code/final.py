from multiprocessing import Pool#, Lock
from time import time

#l = Lock()


class fooclass:
	def __init__(self):
		self.var = 5

	def foo(self, i):
		#l.acquire()
		ans = 0
		for j in range(1,1000000):
			ans += self.var * (i+j) ** 172.384 ** (1 / i**2.3242)
		#l.release()
		return ans


class wrapper:

	def __init__(self, obj, pool):
		self.obj = obj
		self.pool = pool

	def __getattr__(self, name):
		def closure(*args):
			return self.pool.apply_async(getattr(self.obj, name), args)
		return closure



if __name__ == '__main__':


	# print("\n\nmulitple runs with indiviual calls : \n")
	# currtime1 = time()

	# for i in range(1,11):
	# 	r1 = fooclass().foo(60*10*i) 
	# 	print(r1)
	# print (time() - currtime1)
	# print()



	pool = Pool(processes = 4)
	currtime2 = time()

	results = []
	for j in range(1,11):
		results.append(wrapper(fooclass(), pool).foo(60*10*j))

	



	r2 = []
	for j in range(10):
		r2.append(results[j].get())
		print(str(r2))
	print (time() - currtime2)
