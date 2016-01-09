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

total_list = [0]


for i in range(1, 1000000):
  total_list = total_list + to_list(i)
  if len(total_list) > 100000 and float(len(total_list))/100000.0 == len(total_list)/100000 :
    print len(total_list)
  if len(total_list) > 1000000:
    break

print len(total_list)
print total_list[1] * total_list[10] * total_list[100] * total_list[1000] * total_list[10000] * total_list[100000] * total_list[1000000]