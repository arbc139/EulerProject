import operator
import math

def is_prime(a):
    return all(a % i for i in xrange(2, a))

def sieveOfAtkin(limit):
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P


L = 1000000
primes = sieveOfAtkin(L/100)

prime_sum = []

# find all of sigma in primes (sigma_n to prime)
for p in primes:
  if not prime_sum:
    prime_sum.append(p)
    continue
  if prime_sum[-1]+p >= L: break
  prime_sum.append(prime_sum[-1] + p)


c = len(prime_sum)
print 'prime_sum!!!!!!!!!!!!', len(prime_sum)

max_prime = 0
terms = 1

for i in xrange(c):
  print i, '\t', c-1, i+terms, '\t<<<<<<<<#### terms:', terms, max_prime
  for j in xrange(c-1, i+terms, -1):
    n = prime_sum[j] - prime_sum[i]
    if (j-i > terms and is_prime(n)):
      terms, max_prime = j-i, n
      break

# print "Project Euler 50 Solution = ", max_prime, " with ", terms, " terms"

"""
partial_sum_of_prime = dict()

max_len = 0

for idx, prime in enumerate(primes):
  if prime > 1000:
    if float(idx)/10000.0 == idx/10000: print '#################### i gogo: ', idx
    for j in range(0, idx):
      for k in range(j+1, idx):
        if max_len > k-j:
          continue
        if prime < sum(primes[j:k]):
          break
        elif prime == sum(primes[j:k]):
          if prime in partial_sum_of_prime:
            if len(primes[j:k]) > partial_sum_of_prime[prime]:
              partial_sum_of_prime[prime] = len(primes[j:k])
          else:
            partial_sum_of_prime[prime] = len(primes[j:k])
          if max_len < len(primes[j:k]): max_len = len(primes[j:k])


print sorted(partial_sum_of_prime.items(), key=operator.itemgetter(0))
"""