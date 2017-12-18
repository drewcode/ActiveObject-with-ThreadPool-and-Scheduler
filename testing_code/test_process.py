from multiprocessing import Pool
from time import time

class fooclass:
	def __init__(self):
		self.var = 5

	def foo(self, i):
		ans = 0
		i = i + 1
		for j in range(1,1000000):
			ans += self.var * i ** 172.384 ** (1 / i**2.3242)
			ans = ans / j
		return ans



class wrapper:
	def __init__(self, obj):
		self.obj = obj

	def __getattr__(self, name):
		attr = getattr(self.obj, name)
		return attr



if __name__ == '__main__':

	# print("single timings to see overhead : \n")
	# currtime1 = time()
	# r1 = wrapper(fooclass()).foo(60*10) #[fooclass().foo(i*10) for i in range(2,6)]
	# print(r1)
	# print (time() - currtime1)

	# print()

	# currtime2 = time()	
	# pool = Pool(processes = 4)
	# results = pool.apply_async(wrapper(fooclass()).foo, [60*10]) #pool.map_async(fooclass().foo, [i*10 for i in range(2,6)])
	# r2 = results.get()
	# print(r2)
	# print (time() - currtime2)

	# print(results)



	print("\n\nmulitple runs with indiviual calls : \n")
	currtime1 = time()
	for i in range(10):
		r1 = wrapper(fooclass()).foo(60*10*i) #[fooclass().foo(i*10) for i in range(2,6)]
		print(r1)
	print (time() - currtime1)

	print()

	currtime2 = time()	
	pool = Pool(processes = 4)
	results = []
	for j in range(10):
		results.append(pool.apply_async(wrapper(fooclass()).foo, [60*10*j])) #pool.map_async(fooclass().foo, [i*10 for i in range(2,6)])
	
	r2 = []
	for j in range(10):
		r2.append(results[j].get())
		print(str(r2))
	print (time() - currtime2)





	# print("\n\nWith 10 payloads : \n")
	# currtime1 = time()
	# r1 = [fooclass().foo(i*100) for i in range(2,12)]
	# print(r1)
	# print (time() - currtime1)

	# print()

	# currtime2 = time()	
	# pool = Pool(processes = 4)
	# results = pool.map_async(fooclass().foo, [i*100 for i in range(2,12)])
	# r2 = results.get()
	# print(r2)
	# print (time() - currtime2)
	# print()

