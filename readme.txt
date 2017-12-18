1. "from Fooclass import fooclass"
Or from any module of choice, import a class

2. "from Wrapper import wrapper"
Import the wrapper class, this will have to be initialised with the object and a schduler

3. "from Scheduler import scheduler"
Import Scheduler of choice

4. Initialise a reference to a scheduler first
"s = scheduler"
Now set the number of threads
"s.number_of_processes(4)"

5. Create an object of your class and wrap it along with passing it the scheduler
"f = wrapper(fooclass(), s)"

6. Call whatever method(of your class) on the wrapped object
"result = f.foo(455661)"
Store the return object, it is a future of sorts

7. Retrieve the result of the operation at any later time with :
"result.get()"