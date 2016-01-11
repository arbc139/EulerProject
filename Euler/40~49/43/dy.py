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

def test_partialList(pand):
  prime_dict = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13, 7:17}
  for i in range(1, 8):
    partial_list = pand[i:i+3] # i, i+1, i+2
    if to_number(partial_list) % prime_dict[i] != 0: return False

  return True




answer = set()

pand_base = set([0,1,2,3,4,5,6,7,8,9])
pand_permutation = permutations(pand_base, 10)

test_partialList([1,2,3,4,5,6,7,8,9,0])

for pand in pand_permutation:
  if pand[0] == 0: continue
  elif test_partialList(pand): answer.add(to_number(pand))

print answer
print sum(answer)
