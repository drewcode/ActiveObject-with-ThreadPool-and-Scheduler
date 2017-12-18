
class fooclass:
	def __init__(self):
		self.var = 5

	def foo(self):
		print(self.var)

class wrapper:
	def __init__(self):
		self.f = fooclass()

	def __getattr__(self, name):
		attr = getattr(self.f, name)
		return attr

w = wrapper()
w.foo()