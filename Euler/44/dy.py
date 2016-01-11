def getPentaSet(n):
  penta_set = set()
  for i in range(1, n):
    penta_set.add( i*(3*i-1)/2 )

  return penta_set

SET_SIZE = 10000

penta_set = getPentaSet(SET_SIZE)
answer = set()

for p_j in penta_set:
  for p_k in penta_set:
    if p_j == p_k: continue
    p_diff = abs(p_j - p_k)
    p_sum = p_j + p_k
    if p_diff in penta_set and p_sum in penta_set:
      answer.add(p_diff)

print answer
print min(answer)