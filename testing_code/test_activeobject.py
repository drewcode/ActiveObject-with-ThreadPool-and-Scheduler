
class Pair:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def sum(self):
		return self.a + self.b
	

class Pair2:
	def __init__(self, a):
		self.a = a

	def sum(self, b):
		return self.a + b


class Wrapper:
	def __init__(self, obj):
		self.obj = obj

	def __getattr__(self, name, *args, **kwargs):
		attr = getattr(self.obj, name)
		print(attr)
		if callable(attr):
			return getattr(self.obj, name)(*args, **kwargs)
		else:
			return attr

	# def __call__(self, *args, **kwargs):
	# 	return getattr(self.obj)


# p1 = Pair(5,10)
# print (p1.a)
# print()

# w1 = Wrapper(Pair(5,10))
# print(w1.a)
# print()

# p1 = Pair(5,10)
# print (p1.sum())
# print()

# w1 = Wrapper(Pair(5,10))
# print(w1.sum())
# print()


p2 = Pair2(5)
print (p2.sum(10))
print()

w2 = Wrapper(Pair2(5))
print(w2.sum(10))


