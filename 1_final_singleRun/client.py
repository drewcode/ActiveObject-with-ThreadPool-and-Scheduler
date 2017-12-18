from time import time

from Fooclass import fooclass
from Wrapper import wrapper
from Scheduler import scheduler


if __name__ == '__main__':
	
	s = scheduler
	s.number_of_processes(4)

	foo_obj = fooclass()
	wrapped_foo_obj = wrapper(foo_obj, s)


	result_future = wrapped_foo_obj.foo(600)
	result = result_future.get()

	print(result)


	res = wrapper(fooclass(), s).foo(455661)
	result = res.get()

	print(result)

