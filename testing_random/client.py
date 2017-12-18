from time import time

import math
from Wrapper import wrapper
from Scheduler import scheduler


if __name__ == '__main__':
	
	#Without parallelizing

	currtime2 = time()

	results = []
	for i in range(1,100001):
		results.append(math.gcd(i,124230))

	r2 = []
	for i in range(100000):
		r2.append(results[i])
		#print(str(r2))

	print ("\nTime Without parallelizing : ")
	print (time() - currtime2)
	print ("\n\n")


	#With parallelizing, 4 threads

	s1 = scheduler
	s1.number_of_processes(4)

	currtime2 = time()

	results = []
	for i in range(1,100001):
		results.append(wrapper(math, s1).gcd(i,124230))

	r2 = []
	for i in range(100000):
		r2.append(results[i].get())
		#print(str(r2))

	print ("\nTime Utilizing 4 threads : ")
	print (time() - currtime2)
	print ("\n\n")


	