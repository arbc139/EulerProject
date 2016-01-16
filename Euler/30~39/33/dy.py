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



def test_number(i, j):
  base = Fraction(i) / Fraction(j)

  i_digits = to_list(i)
  j_digits = to_list(j)

  compare = 0
  if i_digits[0] == j_digits[1]:
    if j_digits[0] == 0: return False
    compare = Fraction(i_digits[1]) / Fraction(j_digits[0])
  elif i_digits[1] == j_digits[0]:
    if j_digits[1] == 0: return False
    compare = Fraction(i_digits[0]) / Fraction(j_digits[1])
  else:
    return False

  if base == compare:
    return True
  else:
    return False





answers = list()

# i / j
for i in range(10, 100):
  for j in range(i+1, 100):
    print i, j
    if test_number(i, j):
      answers.append( Fraction(i) / Fraction(j) )

print answers

final_answer = None
for answer in answers:
  if final_answer == None:
    final_answer = answer
  else:
    final_answer = final_answer * answer

print final_answer