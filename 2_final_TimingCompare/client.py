from time import time

from Fooclass import fooclass
from Wrapper import wrapper
from Scheduler import scheduler


if __name__ == '__main__':
	
	#Without parallelizing

	currtime2 = time()

	results = []
	for i in range(1,11):
		results.append(fooclass().foo(60*10*i))

	r2 = []
	for i in range(10):
		r2.append(results[i])
		print(str(r2))

	print ("\nTime Without parallelizing : ")
	print (time() - currtime2)
	print ("\n\n")



	#With parallelizing, 2 threads

	s2 = scheduler
	s2.number_of_processes(2)

	currtime2 = time()

	results = []
	for i in range(1,11):
		results.append(wrapper(fooclass(), s2).foo(60*10*i))

	r2 = []
	for i in range(10):
		r2.append(results[i].get())
		print(str(r2))

	print ("\nTime Utilizing 2 threads : ")
	print (time() - currtime2)
	print ()



	#With parallelizing, 4 threads

	s1 = scheduler
	s1.number_of_processes(4)

	currtime2 = time()

	results = []
	for i in range(1,11):
		results.append(wrapper(fooclass(), s1).foo(60*10*i))

	r2 = []
	for i in range(10):
		r2.append(results[i].get())
		print(str(r2))

	print ("\nTime Utilizing 4 threads : ")
	print (time() - currtime2)
	print ("\n\n")