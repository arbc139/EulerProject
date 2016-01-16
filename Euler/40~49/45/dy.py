from math import sqrt

SIZE = 100000000

def axiomOfRoot(a,b,c):
  first = (-(b) + sqrt(b**2 - (4*a*c))) / (2*a)
  second = (-(b) - sqrt(b**2 - (4*a*c))) / (2*a)

  return (first, second)

# penta = n(3n-1)/2
def isPenta(k):
  # find solution of '3n**2 - n - 2*k = 0'
  a = 3
  b = -1
  c = -2*k

  # axiom of root
  solutions = axiomOfRoot(a,b,c)
  if (solutions[0]).is_integer():
    print 'Penta:', k
    return True
  else:
    return False

def getPenta(k):
  return k*(3*k-1)/2

# hexa = n(2n-1)
def isHexa(k):
  # find solution of '2*n**2 - n - k = 0'
  a = 2
  b = -1
  c = -1*k

  # axiom of root
  solutions = axiomOfRoot(a,b,c)
  if (solutions[0]).is_integer():
    print 'Hexa:', k
    return True
  else:
    return False

def getHexa(k):
  return k*(2*k-1)

answer = set()

i = 100
count = 0
while True:
  tri = i*(i+1)/2
  if isPenta(tri) and isHexa(tri):
    answer.add(tri)
    print tri
    count += 1
    if count == 2:
      break
  i += 1


print answer