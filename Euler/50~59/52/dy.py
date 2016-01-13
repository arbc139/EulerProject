import math

def combination(factorial_dict, n, r):
  if n < r: return False
  return factorial_dict[n] / (factorial_dict[r] * factorial_dict[n-r])

answer = list()
SIZE = 1000000


factorial_dict = dict()

for i in range(0, 101):
  factorial_dict[i] = math.factorial(i)


for n in range(1, 101):
  for r in range(0, n+1):
    if combination(factorial_dict, n, r) > SIZE:
      answer.append([n, r])

print answer
print len(answer)