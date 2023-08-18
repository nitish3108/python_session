num = 1
while num <= 100:
	if ( num % 3 == 0 ) and ( num % 5 == 0 ):
		print("Fifteen")
	elif num % 3 == 0:
		print("Three")
	elif num % 5 == 0:
		print("Five")
	else:
		print(num)
	num += 1

