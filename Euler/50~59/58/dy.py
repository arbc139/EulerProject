"""
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
"""

# 1  3  13  31
#  2  10  18

# order_1[0] = 2
# order_1[i] = order_1[i-1] + 8
# order_1[i] = 8*i + 2

# d_1[0] = 1
# d_1[i] = d_1[i-1] + order_1[i-1]
# d_1[i] = d_1[i-1] + 8*(i-1) + 2



# 1  5  17  37
#  4  12  20

# order_2[0] = 4
# order_2[i] = order_2[i-1] + 8
# order_2[i] = 8*i + 4

# d_2[0] = 1
# d_2[i] = d_2[i-1] + order_2[i-1]
# d_2[i] = d_2[i-1] + 8*(i-1) + 4



# 1  7  21  43
#  6  14  22

# order_3[0] = 6
# order_3[i] = order_3[i-1] + 8
# order_3[i] = 8*i + 6

# d_3[0] = 1
# d_3[i] = d_3[i-1] + order_3[i-1]
# d_3[i] = d_3[i-1] + 8*(i-1) + 6



# 1  9  25  49
#  8  16  24



# side length
# 1  3  5  7  9 ...

# side[0] = 1
# side[i] = side[i-1] + 2
# side[i] = 2*(i+1)-1

# side[0] = 1


# whole set size
# 1  5  9  13
# set_size[0] = 1
# set_size[i] = set_size[i-1] + 4

# set_size[i] = 4*(i+1) - 3

import random

# is_prime function
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



SIZE = 100000
answer = 0

d_1 = [1]
d_2 = [1]
d_3 = [1]

def get_side_len(i):
  return 2*(i+1)-1

def get_whole_set_size(i):
  return 4*(i+1)-3

def get_ratio(prime_set_size, whole_size):
  return float(prime_set_size) / float(whole_size) * 100

def order(num, i):
  return 8*i + 2*num


prime_set = set()

for i in range(1, SIZE):
  new_d_1 = d_1[i-1] + order(1, i-1)
  new_d_2 = d_2[i-1] + order(2, i-1)
  new_d_3 = d_3[i-1] + order(3, i-1)

  if is_prime(new_d_1):
    prime_set.add(new_d_1)
  if is_prime(new_d_2):
    prime_set.add(new_d_2)
  if is_prime(new_d_3):
    prime_set.add(new_d_3)

  ratio = get_ratio(len(prime_set), get_whole_set_size(i))

  if ratio < 10:
    print get_side_len(i)
    break

  d_1.append(new_d_1)
  d_2.append(new_d_2)
  d_3.append(new_d_3)


