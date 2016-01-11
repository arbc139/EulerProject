import operator

def possible_triangle_list(n):
  tri_list = list()

  # 1 <= a <= n-2
  for a in range(1, n/3+1):
    # 1 <= b <= n-1-a
    for b in range(1, n-a):
      c = n-a-b
      if b < a or c < b: continue
      if isTriangle(a,b,c):
        tri_list.append([a,b,c])

  return tri_list

def isTriangle(a,b,c):
  return (a**2+b**2) == c**2

print possible_triangle_list(120)

answer = dict()

for i in range(3, 1001):
  answer[i] = len(possible_triangle_list(i))

print sorted(answer.items(), key=operator.itemgetter(1))
