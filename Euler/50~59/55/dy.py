answer = list()
SIZE = 10000

def is_palindrome(n):
  return is_list_palindrome(to_list(n))

def is_list_palindrome(n_list):
  for i in range(0, len(n_list)/2):
    if n_list[i] != n_list[-(i+1)]: return False
  return True

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



def is_lychrel(n):
  def reverse(n):
    listed_n = to_list(n)
    listed_n.reverse()
    return to_number(listed_n)

  # 50 iteration
  for i in xrange(50):
    summed = n + reverse(n)
    if is_palindrome(summed):
      return False
    else:
      n = summed

  return True


for i in range(1, SIZE+1):
  if is_lychrel(i):
    answer.append(i)


print answer
print len(answer)


