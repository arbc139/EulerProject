import os

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


f = open(os.path.expanduser("~/Documents/Development/Python/Project/Euler/input/13.txt"), "r")

numbers = []

while True:
  line = f.readline()
  if not line: break

  numbers.append(long(line))


print numbers

number_list = to_list(sum(numbers))

print to_number(number_list[0:10])