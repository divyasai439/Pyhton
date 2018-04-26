def PrimeNumbers(N):
	for n in range(2,N):
		for x in range(2,n):
			if n%x == 0:
				break
		else:
			print(n, "is a prime number")
PrimeNumbers(10)