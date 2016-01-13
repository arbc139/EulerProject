import random
import itertools
answer = set()
SIZE = 6 # digit size

_mrpt_num_trials = 5 # number of bases to test

# list to number
def to_number(n_list):
  final_number = 0
  for (idx, num) in enumerate(n_list):
    rdx = len(n_list) - idx - 1
    final_number = final_number + (num * 10**rdx)
  return final_number

# prime test
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

def unique(iterable):
    seen = set()
    for x in iterable:
        if x in seen:
            continue
        seen.add(x)
        yield x


shuffle_list = set([0,1,2,3,4,5,6,7,8,9])


# assume 8 has 6 digit size
# n is '*' digit size!
# ex) n=2, comb_size=4
#    --> 1234**
def test():
  for n in range(2, SIZE+1):
    comb_size = SIZE-n
    combs = itertools.combinations_with_replacement(shuffle_list, comb_size)
    for comb in combs:
      box = list(comb)
      # [0,1,2,3]
      # 0 1 2 3

      for i in range(0, n):
        box.append('*')

      for case in unique(itertools.permutations(box, SIZE)):
        if case[0] == 0: continue
        answer_set = list()

        for num in range(0, 10):
          candidate = map(lambda x:x if x!= '*' else num, case)
          if candidate[-1]%2 == 0 or candidate[0] == 0: continue
          test_number = to_number(candidate)
          if test_number == 121313:
            print case
          if is_prime(test_number):
            answer_set.append(test_number)

        if len(answer_set) == 8:
          print sorted(answer_set)
          return True

  return False


print test()





