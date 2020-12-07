#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

min = 10
max = 10
smallestNumber = 999999999

#for i in range(min, 

i = min

def getPrimeNumbers(upperBound):
	primes = [2]
	
	for i in range(3, upperBound):
		prime = True
		for j in range(2, i):
			if i % j == 0:
				prime = False
				break
		if prime:		
			primes.append(i)
	return primes

numbersToDivideWith = getPrimeNumbers(max)

while True:
	moduloNumbers = list(map((lambda x: i % x == 0), numbersToDivideWith))
	if all(moduloNumbers):
		smallestNumber = i
		break
	i = i + 1
print(smallestNumber)		
		
	