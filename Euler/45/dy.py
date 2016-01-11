from math import sqrt

SIZE = 10000000000

# tri = n(n+1)/2
def getTriSet(n):
  tri_set = set()
  for i in range(1, SIZE):
    tri_number = i*(i+1)/2
    if tri_number > n: break
    else: tri_set.add(tri_number)
  return tri_set

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
  if getPenta(long(solutions[0]))==k or getPenta(long(solutions[0])+1)==k:
    print 'Penta: ', k
    return True
  else:
    return False
  """
  if (solutions[0]).is_integer():
    return True
  else:
    return False
  """

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
  if getHexa(long(solutions[0]))==k or getHexa(long(solutions[0])+1)==k:
    print 'Hexa: ', k
    return True
  else:
    return False
  """
  if (solutions[0]).is_integer():
    return True
  else:
    return False
  """

def getHexa(k):
  return k*(2*k-1)

tri_set = getTriSet(SIZE)

answer = set()


for index, tri in enumerate(tri_set):
  #if float(index)/100000000.0 == index/100000000: print 'gogo: ', index
  if isPenta(tri) and isHexa(tri):
    answer.add(tri)


print answer