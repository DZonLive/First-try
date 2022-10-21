def decorate(funct):
	def wrapper(value):
		print('wrapper')
		funct(value)
	return wrapper

@decorate
def test(value):
	print(f"test, value: {value}")

test('value in test')