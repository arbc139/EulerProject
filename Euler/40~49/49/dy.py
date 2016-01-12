def factor(n):
  if n==1: return [1]
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


def is_permutation(primes):
  permutation_set = set(to_list(primes[0]))

  for prime in primes:
    if permutation_set != set(to_list(prime)):
      return False
  return True


answer = list()

primes = list()

for i in range(1000, 10000):
  if isPrime(i):
    primes.append(i)


progressions = list()

for i in range(0, len(primes)-2):
  first = primes[i]
  for j in range(i+1, len(primes)-1):
    second = primes[j]
    interval = second - first
    for k in range(j+1, len(primes)):
      third = primes[k]
      if third-second != interval:
        continue
      else:
        progressions.append([first,second,third])


for progression in progressions:
  if is_permutation(progression):
    answer.append(progression)


print answer