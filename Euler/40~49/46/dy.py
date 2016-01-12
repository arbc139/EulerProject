# a = b + 2 * c^2

# a > b
# a is odd composite
# b is prime

# c = sqrt(1/2 * (a-b))

from math import sqrt

def factor(n):
  if n==1 or n==0: return False
  i = 2
  limit = n**0.5    # max root of n
  while i<=limit:
    if n%i == 0:  # if i is divisor of n
      return False  # return ret!
    i += 1

  return [n]      # if n is prime, return that(base case)

def isPrime(n):
  if not factor(n): return False
  else: return True

def goldbah_guess(n, primes):
  for prime in primes:
    if prime >= n: break
    elif (sqrt((n - prime)/2)).is_integer(): return True
    else: continue

  return False


SIZE = 10000
answer = set()
not_answer = set()



primes = list()
composites = list()
for i in range(2, SIZE):
  if isPrime(i):
    primes.append(i)
  elif i%2 == 1:
    composites.append(i)


for composite in composites:
  if not goldbah_guess(composite, primes):
    answer.add(composite)
  else:
    not_answer.add(composite)


print not_answer
print answer

