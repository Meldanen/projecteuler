# The sum of the squares of the first ten natural numbers is 385,

# The square of the sum of the first ten natural numbers is 3025,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

max = 100

numberList = range(1, max + 1)

sumOfSquare = sum(item ** 2 for item in range(1, max + 1))
squareOfSums = sum(item for item in range(1, max + 1)) ** 2

print(sumOfSquare)
print(squareOfSums)
print(squareOfSums - sumOfSquare)

# Answer : 25164150
