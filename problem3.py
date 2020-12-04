#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
factor = -1
maxNumber = 600851475143
def isPrime(number):
	for j in range(2, number):
		if number % j  == 0:
			return False
	else:
		return True

for i in range(3, maxNumber):
	if isPrime(i) and maxNumber % i == 0:
		factor = i
		print(factor)
print(factor)
# Answer: 6857


