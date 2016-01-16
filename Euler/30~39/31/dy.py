# DP

coins = [1, 2, 5, 10, 20, 50, 100, 200]
target_money = 200

ways = [0 for i in xrange(target_money+1)]
ways[0] = 1

print 'coin', '\ti', '\tways'
for coin in coins:
  for i in range(coin, target_money+1):
    ways[i] += ways[i-coin]
    print coin, '\t', i, '\t', ways[i]


# 해설
"""
  <첫번째 for문>
    coin별로 가능한 target_money를 축적해간다. (사용하는 coin 개수를 늘림)
    ex) coin == 1이고 for i in range(coin, target_money+1)에선 ways[i]가 i money를 coin 1개로만 만드는 방법을 구한다.

  결국엔 coin수와 money에 대해 DP를 적용시켰다고 할 수 있다.
"""