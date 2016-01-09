# number to list
def to_list(n):
  if n < 10:
    return [n]
  else:
    result = to_list(n/10)
    result.append(n%10)
    return result

# list to number
def to_number(n_list):
  final_number = 0
  for (idx, num) in enumerate(n_list):
    rdx = len(n_list) - idx - 1
    final_number = final_number + (num * 10**rdx)
  return final_number


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
  if n==1 or not factor(n): return False
  else: return True

# permutation
def permutations(iterable, r=None):
  pool = tuple(iterable)
  n = len(pool)
  r = n if r is None else r
  if r > n:
    return
  indices = range(n)
  cycles = range(n, n-r, -1)
  yield tuple(pool[i] for i in indices[:r])
  while n:
    for i in reversed(range(r)):
      cycles[i] -= 1
      if cycles[i] == 0:
        indices[i:] = indices[i+1:] + indices[i:i+1]
        cycles[i] = n - i
      else:
        j = cycles[i]
        indices[i], indices[-j] = indices[-j], indices[i]
        yield tuple(pool[i] for i in indices[:r])
        break
    else:
      return

answer = set()

for i in range(1, 10):
  permutation_list = []
  for n in range(1, i+1):
    permutation_list.append(n)
  pandigitals = permutations(permutation_list, i)
  for pand in pandigitals:
    pand_number = to_number(pand)
    if isPrime(pand_number):
      answer.add(pand_number)

print answer
print max(answer)