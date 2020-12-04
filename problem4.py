#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.
def isPalindrome(number):
	numberString = str(number)
	return numberString == numberString[::-1]

min = 100
max = 1000
bestPalindrome = -1
factors = []
for i in range(min, max):
	for j in range(min, max):
		product = i * j
		if (isPalindrome(product)):
			if bestPalindrome < product:
				bestPalindrome = product
				factors = [i, j]
print(bestPalindrome)
print(factors)

# Answer: 906609 by [913, 993] 