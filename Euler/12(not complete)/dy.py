def GetTriNumber(n):
	sum = 0
	for i in range(1, n+1):
		sum += i
	return sum

def getDivisors(n):
	list = []
	for i in range(1, n+1):
		if n%i == 0:
			list.append(i)
	return list

i = 0

while True:
	i += 1

	n = GetTriNumber(i)
	divisorList = getDivisors(n)
	if len(divisorList) >= 500:
		print(n)
		break