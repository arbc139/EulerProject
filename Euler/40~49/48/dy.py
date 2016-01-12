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


answer = list()

print 'total_sum started'

total_sum = 0
for i in range(1, 1001):
  total_sum += i**i

print 'total_sum finished'

listed_sum = to_list(total_sum)
answer = listed_sum[len(listed_sum)-10:]

print answer

print to_number(answer)