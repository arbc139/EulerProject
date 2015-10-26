def getCircular(n):
    circularList = []
    remainder = 1

    testCircularFlag = False
    additionalCircular = []

    while True:
        if testCircularFlag:
            additionalCircular.append(remainder*10/n)
            remainder = remainder*10%n

            if additionalCircular == circularList:
                return additionalCircular

            if additionalCircular[len(additionalCircular)-1] != circularList[len(additionalCircular)-1]:
                testCircularFlag = False
                circularList.append(additionalCircular)
            
        else:
            circularList.append(remainder*10/n)
            remainder = remainder*10%n
