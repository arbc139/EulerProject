# 999 - 99 / 100
# 99 - 9 / 10


def lettering(n):
	if n==1000:	return len("one") + len("Thousand")
	if n>=100 and n<=999:
		result = 0
		dig = (n - n%100)/100
		print("(100~999)\t%d:\t%d" %(n, dig))
		if n != (n/100)*100:
			result += len("and")
		result += digit(dig)+ len("hundred") + lettering(n - (n/100)*100)
		return result
	elif n>=20 and n<=99:
		dig = (n - n%10)/10
		print("(20~99)\t\t%d:\t\t%d" %(n, dig))
		return twenDigit(dig) + lettering(n - (n/10)*10)
	elif n>=10 and n<=19:
		print("(10~19)\t\t%d:\t\t%d" %(n, n))
		return tenDigit(n)
	elif n>=1 and n<=9:
		print("(1~9)\t\t\t%d:\t\t%d" %(n, n))
		return digit(n)
	else:	return 0

def twenDigit(n):
	if n==2:	return len("twenty")
	elif n==3:	return len("thirty")
	elif n==4:	return len("forty")
	elif n==5:	return len("fifty")
	elif n==6:	return len("sixty")
	elif n==7:	return len("seventy")
	elif n==8:	return len("eighty")
	elif n==9:	return len("ninety")

def tenDigit(n):
	if n==10:	return len("ten")
	elif n==11:	return len("eleven")
	elif n==12:	return len("twelve")
	elif n==13:	return len("thirteen")
	elif n==14:	return len("fourteen")
	elif n==15:	return len("fifteen")
	elif n==16:	return len("sixteen")
	elif n==17:	return len("seventeen")
	elif n==18:	return len("eighteen")
	elif n==19:	return len("nineteen")


def digit(n):
	if n==1: 	return len("one")
	elif n==2:	return len("two")
	elif n==3: 	return len("three")
	elif n==4:	return len("four")
	elif n==5:	return len("five")
	elif n==6: 	return len("six")
	elif n==7:	return len("seven")
	elif n==8:	return len("eight")
	elif n==9:	return len("nine")
	else:  return 0

sum = 0

for i in range(1, 1001):
	sum += lettering(i)

print(sum)

print lettering(342)