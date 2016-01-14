from fractions import Fraction

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



# a[i] = 1 + 1/d[i]


# d[0] = 2
# d[1] = 2 + 1/2
# d[2] = 2 + 1/(2 + 1/2)
# ...
# d[i+1] = 2 + 1/d[i] (d[0] == 2)


answer = list()

a = []

d = [Fraction(2)]
a.append(Fraction(1) + (Fraction(1) / d[0]))


for i in range(1, 1001):
  d.append(Fraction(2) + (Fraction(1) / d[i-1]))
  a.append(Fraction(1) + (Fraction(1) / d[i]))

  if len(to_list(a[i].numerator)) > len(to_list(a[i].denominator)):
    answer.append(a[i])


print answer
print len(answer)