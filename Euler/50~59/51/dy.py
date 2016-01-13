import math
import operator

def is_prime(a):
    return all(a % i for i in xrange(2, a))

# number to list
def to_list(n):
  if n < 10:
    return [n]
  else:
    result = to_list(n/10)
    result.append(n%10)
    return result

def get_digit_counter(n_list):
  digit_dict = dict()

  for element in n_list:
    if element in digit_dict:
      digit_dict[element] += 1
    else:
      digit_dict[element] = 1

  return sorted(digit_dict.items(), key=operator.itemgetter(0))


# list to number
def to_number(n_list):
  final_number = 0
  for (idx, num) in enumerate(n_list):
    rdx = len(n_list) - idx - 1
    final_number = final_number + (num * 10**rdx)
  return final_number

def is_permutable(source, target):
  source_list = to_list(source)
  target_list = to_list(target)

  if len(source_list) != len(target_list):
    return False

  source_digit_counter = get_digit_counter(source_list)
  target_digit_counter = get_digit_counter(target_list)

  if source_digit_counter == target_digit_counter:
    return True
  else:
    return False

def is_possible(n):
  for count in range(2, 7):
    if not is_permutable(n, count*n):
      return False

  return True


SIZE = 1000000

for i in range(10, SIZE):
  if is_possible(i):
    print i
    break
