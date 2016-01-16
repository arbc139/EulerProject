import math
import itertools
import random


_mrpt_num_trials = 5 # number of bases to test
def is_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
    return True # no base tested showed n as composite


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

# number to list
def to_list(n):
  if n < 10:
    return [n]
  else:
    result = [n%10]
    while n >= 10:
      n = n /10
      result.append(n%10)
    result.reverse()
    return result

# list to number
def to_number(n_list):
  final_number = 0
  for (idx, num) in enumerate(n_list):
    rdx = len(n_list) - idx - 1
    final_number = final_number + (num * 10**rdx)
  return final_number


def test_problem(primes):
  def link_prime(first, second):
    first_list = to_list(first)
    second_list = to_list(second)
    return to_number(first_list + second_list)

  for i in range(0, len(primes)):
    for j in range(0, len(primes)):
      if i==j: continue
      linked = link_prime(primes[i], primes[j])

      if not is_prime(linked):
        return False

  return True




PRIME_SIZE = 10000
answer = set()

test_primes = sieveOfAtkin(PRIME_SIZE)

print 'good?'


def find_possible_set(size):
  if size == 2:
    combs = itertools.combinations(test_primes, size)

    before_list = []

    for comb in combs:
      if test_problem(comb):
        before_list.append(comb)

    return before_list

  else:
    before_list = find_possible_set(size-1)

    new_list = []

    for before in before_list:
      for prime in test_primes:
        if prime in before:
          continue
        else:
          cand = set(before)
          cand.add(prime)

          if not(cand in new_list) and test_problem(list(cand)):
            new_list.append(cand)
            if size == 5:
              return sum(cand)

    return new_list

print find_possible_set(5)


print answer
