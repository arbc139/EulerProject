import operator

def factor(n):
  if n==1: return [1]
  i = 2
  limit = n**0.5    # max root of n
  while i<=limit:
    if n%i == 0:  # if i is divisor of n
      return False  # return ret!
    i += 1

  return n    # if n is prime, return that(base case)

def isPrime(n):
  if not factor(n): return False
  else: return n

answer = dict()


# 10^k =. 1 (mod n)
# => 10^k mod n = 1 mod n
# => 10^k mod n = 1
for n in range(2, 1001):
  if n==2 or n==5 or not isPrime(n):
    continue
  else:
    k = 1
    while 10**k % n != 1:
      if k > 30:
        print 'infinite loop? ', k, ', ', n
      k += 1
    answer[n] = k

sorted_answer = sorted(answer.items(), key=operator.itemgetter(1))

print sorted_answer