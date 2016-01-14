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


max_digit_sum = 0
answer = 0

for b in range(1, 101):
  for a in range(1, 101):
    num = a**b
    digit_sum = sum(to_list(num))
    if max_digit_sum < digit_sum:
      answer = num
      max_digit_sum = digit_sum



print answer
print max_digit_sum
