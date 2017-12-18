class fooclass:
	def __init__(self):
		self.var = 5

	def foo(self, i):
		ans = 0
		for j in range(1,1000000):
			ans += self.var * (i+j) ** 172.384 ** (1 / i**2.3242)
		return ans