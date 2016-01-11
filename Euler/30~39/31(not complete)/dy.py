"""
    *** Divide and Conquer Method ***

def findKindOfCase(totalMoney, coinList):
    # coin list is sorted to ascending order
    localCoinList = list(coinList)

    # base case
    if len(localCoinList) == 1:
        return 1

    totalCase = 0

    theLargestCoin = localCoinList[0]
    coinList.remove(localCoinList[0])

    # cases
    while True:
        totalCase += findKindOfCase(totalMoney, localCoinList)

        totalMoney -= theLargestCoin
        if totalMoney <= 0:
            break
    return totalCase
"""


coinList = [1,2]#,5,10,20,50,100,200]
totalMoney = 5

numberOfCoins = len(coinList)

# 1,1,1,1,1
# 2,1,1,1
# 2,2,1

# caseByMoney[i][m]
caseByMoney = [[0 for i in range(0, totalMoney+1)] for j in range(0, numberOfCoins+1)]

# Dynamic Programming
caseByMoney[0][0] = 1

for i in range(1, numberOfCoins+1):
    if coinList[0] == i:
        caseByMoney[i][i] = 1
    caseByMoney[i][0] = 1

print(caseByMoney)

for m in range(1, totalMoney+1):
    for coin in coinList:
        if m-coin != 0: continue
        caseByMoney[1][m] = 1

print(caseByMoney)

for i in range(2, numberOfCoins+1):
    for m in range(2, totalMoney+1):
        for coin in coinList:
            if m-coin < 0: continue
            caseByMoney[i][m] += caseByMoney[i-1][m-coin]
            print(i, m, coin, m-coin, "and", caseByMoney[i][m], caseByMoney[i-1][m-coin], caseByMoney)



totalCase = 0

for i in range(1, numberOfCoins+1):
    totalCase += caseByMoney[i][totalMoney]

print(totalCase)