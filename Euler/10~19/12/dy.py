import math

def GetTriNumber(n):
	return n*(n+1)/2

"""
def getDivisors(n):
	list = []
	for i in range(1, n+1):
		if n%i == 0:
			list.append(i)
	return list
"""

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

i = 0

while True:
	i += 1

	n = GetTriNumber(i)
	divisorList = list(divisorGenerator(n))
	if len(divisorList) >= 500:
		print(n)
		break